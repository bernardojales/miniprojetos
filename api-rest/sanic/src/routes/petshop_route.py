from sanic import Blueprint, Request, response # import the blueprint class

PETSHOP_ROUTE = Blueprint("petshop") # instantiate a blueprint setting his name

#                       uri,     methods    
@PETSHOP_ROUTE.route("/petshop", methods=["GET"]) # define handler to endpoint when METHOD == GET
async def get_petshop2(request: Request): # function name of handler must be unique
    response.json([{"name": "Villa Petshop"}]) # the default status code is 200 and headers are set as {}, we can ommity this parameters


@PETSHOP_ROUTE.route("/petshop", methods=["POST"]) # define handler to endpoint when METHOD == POST
async def create_petshop(request: Request): # function name of handler must be unique
    # LETS GET THE REQUEST BODY CONTENT
    # request.body # get body of request in format bytes
    # request.json # get body of request in json format
    body = request.json or {}
    print(body)
    # LETS ADD SOME VALIDATION FOR THE INPUT CONTENT
    # just accept requests that contain name field
    if "name" in body and not (set(body) - set({"name"})):
        response.json(body) # the default status code is 200 and headers are set as {}, we can ommity this parameters
    else:
        # Sends a error response indicating that the request body is invalid
        response.json({"message": "invalid body", "description": "must only pass the required fields: name"}, status=400)
