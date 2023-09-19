from sanic import Blueprint
from .petshop_route import PETSHOP_ROUTE

ROUTES = Blueprint.group(
    PETSHOP_ROUTE,
)