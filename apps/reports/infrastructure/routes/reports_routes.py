





from datetime import date
from databases import Database
from fastapi import APIRouter, Depends
from fpdf import FPDF
from starlette.responses import FileResponse
from apps.auth.infraestructure.dependecies.auth_dependecies import get_current_active_user
from apps.ingredients.infrastructure.mappers.ingredient_mapper import IngredientMapper
from apps.ingredients.infrastructure.repositories.db_ingredients_repository import DbIngredientsRepository
from apps.order.application.dto.get_sells_in_range_dto import GetSellsInRangeDto
from apps.order.application.services.get_orders_in_range_application_service import GetOrdersInRangeApplicationService
from apps.plates.infrastructure.mappers.plates_mapper import PlateMapper
from apps.plates.infrastructure.repositories.db_plates_repository import DbPlatesRepository
from apps.reports.infrastructure.dto.orders_in_range_dto_entry import OrdersInRangeDtoEntry
from apps.store.application.services.get_store_ingredients import GetStoresIngredientsApplicationService
from apps.store.infrastructure.mappers.store_mapper import StoreMapper
from apps.store.infrastructure.repositories.db_store_repository import DbStoreRepository
from apps.user.infrastructure.db_entity.user_in_db import UserInDB
from apps.user.infrastructure.mappers.user_mapper import UserMapper
from apps.user.infrastructure.repositories.db_user_repository import dbUserRepository
from db.db_dependencies import get_database
from core.application.decorators.exception_decorator import ExceptionDecorator
from apps.order.application.services.get_sells_in_range_application_service import (
    GetSellsInRangeApplicationService)
from apps.order.infrastructure.repositories.db_orders_repository import DbOrdersRepository
from apps.order.infrastructure.mappers.orders_mapper import OrderMapper


report_router = APIRouter(
    prefix="/reports",
    tags=["reports"],
    responses={404: {"description": "Not found"}},
)

@report_router.get("/anualsells/{year}", name="report")
async def AnualSellsReport(
    year: int,
    db: Database = Depends(get_database),
    current_user: UserInDB = Depends(get_current_active_user)
):
    if year < 2000 or year > date.today().year:
        return 'Year must be a valid year.'
    init_dates = []
    end_dates = []
    for i in range(1, 13):
        init_dates.append(date.fromisoformat(f"{year}-{0 if i< 10 else ''}{i}-01"))
        end_dates.append(date.fromisoformat(f"{year + (int(i/12))}-{0 if i+1 < 10 else ''}{i+1 if i<12 else '01'}-01"))
        
    service = ExceptionDecorator(GetSellsInRangeApplicationService(orders_repository=DbOrdersRepository(db, order_mapper=OrderMapper())))
    sells = []
    sells.append(('Month', 'Sells'))
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October','November', 'December']
    for i in range(1, 13):
        sell = (await service.execute(input=GetSellsInRangeDto( begin=init_dates[i-1], end=end_dates[i-1]))).unwrap()
        sells.append((f'{months[i-1]}',f'{sell}$'))
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times", size=16)
    pdf.cell(10, 10, "Restaurant Gestion System", align="L")
    pdf.cell(0, 10, f"fecha: {date.today()}", align="R")
    pdf.set_font("Times", size=30)
    pdf.cell(-190, 40, f"Anual Sales report Year {year}", align = 'C')
    pdf.ln()
    pdf.set_font("Times", size=16)
    
    with pdf.table(text_align="CENTER") as table:
        for data_row in sells:
            row = table.row()
            for datum in data_row:
                row.cell(datum)
    pdf.output(f'sales_report_{year}.pdf')
    return FileResponse(f'sales_report_{year}.pdf', media_type='application/octet-stream',filename=f'sales_report_{year}.pdf')


@report_router.post("/ordersInRange", name="report")
async def OrdersInRangeReport(
    entry: OrdersInRangeDtoEntry,
    db: Database = Depends(get_database),
    current_user: UserInDB = Depends(get_current_active_user)
):
    if entry.from_date < date.fromisoformat('2000-01-01') or entry.from_date > date.today() or entry.to_date < entry.from_date:
        return 'dates must be valid.'
        
    service = ExceptionDecorator(GetOrdersInRangeApplicationService(orders_repository=DbOrdersRepository(db, order_mapper=OrderMapper()),
                                                                    plates_repository=DbPlatesRepository(db, plates_mapper=PlateMapper()),
                                                                    user_repository=dbUserRepository(db, user_mapper=UserMapper())))
    orders = (await service.execute(input=GetSellsInRangeDto( begin=entry.from_date, end=entry.to_date))).unwrap()
    table_orders = []
    table_orders.append(('Order Id', 'Client', 'Plates', 'Price', 'Date'))
    for order in orders:
        plates = ''
        for plate in order.plates:
            plates += f'{plate.name} x{plate.quantity}\n'
        table_orders.append((str(order.id), order.user, plates, f'{order.price}$', order.date))
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times", size=16)
    pdf.cell(10, 10, "Restaurant Gestion System", align="L")
    pdf.cell(0, 10, f"fecha: {date.today()}", align="R")
    pdf.set_font("Times", size=30)
    pdf.cell(-190, 40, f"Orders from {entry.from_date} to {entry.to_date}", align = 'C', new_y='next')
    pdf.set_font("Times", size=14)
    
    with pdf.table(text_align="CENTER") as table:
        for data_row in table_orders:
            row = table.row()
            for datum in data_row:
                row.cell(datum)
    pdf.output(f'orders_from_{entry.from_date}_to_{entry.to_date}_report.pdf')
    return FileResponse(f'orders_from_{entry.from_date}_to_{entry.to_date}_report.pdf', media_type='application/octet-stream',filename=f'orders_from_{entry.from_date}_to_{entry.to_date}_report.pdf')

@report_router.get("/ingredientsInventory", name="report")
async def InventoryReport(
    db: Database = Depends(get_database),
    current_user: UserInDB = Depends(get_current_active_user)
):
    service = ExceptionDecorator(GetStoresIngredientsApplicationService(ingredient_repository=DbIngredientsRepository(db, ingredient_mapper=IngredientMapper())))
    store_repo = DbStoreRepository(db, store_mapper=StoreMapper())
    stores = await store_repo.get_all_stores()
    
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times", size=16)
    pdf.cell(10, 10, "Restaurant Gestion System", align="L")
    pdf.cell(0, 10, f"fecha: {date.today()}", align="R")
    pdf.set_font("Times", size=30)
    pdf.cell(-190, 40, f"Inventory", align = 'C', new_y='next')
    pdf.set_font("Times", size=14)
    for store in stores:
        ingredients = (await service.execute(input=store.id)).unwrap()
        pdf.cell(0, 10, f"Store: {store.name.value}", align="L", new_y='next')
        table_ingredients = []
        table_ingredients.append(('Ingredient', 'Quantity'))
        for ingredient in ingredients:
            table_ingredients.append((ingredient.name.value, str(ingredient.quantity.value)))
        with pdf.table(text_align="CENTER") as table:
            for data_row in table_ingredients:
                row = table.row()
                for datum in data_row:
                    row.cell(datum)
    pdf.output(f'inventory_report_{date.today()}.pdf')
    return FileResponse(f'inventory_report_{date.today()}.pdf', media_type='application/octet-stream',filename=f'inventory_report_{date.today()}.pdf')