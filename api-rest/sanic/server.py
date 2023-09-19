from sanic import Sanic # import Sanic class that represents our API REST application

app = Sanic("http") # instanciate our API REST application

app.route(uri="/petshop", method=["GET"])

if __name__ == "__main__":
    app.run(# run the application passing information
        host="0.0.0.0", # from what network interfaces it must be able to answer
        port=3000, # from what port it must be able to listen
    ) 