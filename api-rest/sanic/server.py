from sanic import Sanic, Request, response # import Sanic class that represents our API REST application

app = Sanic("http") # instanciate our API REST application

@app.route(uri="/petshop", methods=["GET"]) # the basic way to register a endpoint handler
async def get_petshop(request: Request):
    response.text(body="Ok", status=200, headers={}) # Sends a request response with content-type header set as 'text/plain; charset=utf-8'
    # response.json({"message": "Ok"}, status=200, headers={}) # Sends a request response with content-type header set as 'application/json'

# most recommended way to register a endpoint handler
from src.routes import ROUTES # import blueprint group
app.blueprint(ROUTES, version=1)

if __name__ == "__main__":
    from src.utils import settings
    app.run(# run the application passing information
        # host="0.0.0.0", # from what network interfaces it must be able to answer
        # port=3000, # from what port it must be able to listen
        # use environment variables
        host=settings.HOST,
        port= settings.PORT_HTTP
    ) 