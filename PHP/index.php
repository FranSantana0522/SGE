<!doctype html>
<html lang="en">
    <head>
        <title>Formulario ventas</title>
        <!-- Required meta tags -->
        <meta charset="utf-8" />
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1, shrink-to-fit=no"
        />

        <!-- Bootstrap CSS v5.2.1 -->
        <link
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
            rel="stylesheet"
            integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN"
            crossorigin="anonymous"
        />
    </head>

    <body>
        <div class="container-{content}">
        <header>
            <!-- Header  -->
            <div class="container-fluid bg-dark text-light d-flex align-items-center justify-content-center" style="height:10vh">
                <h1>Formulario de ventas</h1>
            </div>
        </header>
        <main>
            <!-- Main div donde esta el formulario -->
            <div class="bg-warning d-flex align-items-center justify-content-center shadow-lg" style="height:80vh">

            <!-- El formulario con el action hacia donde se envian los datos con el metodo post -->
            <form action="listadoVentas.php" method="post" class="mt-3">
                <!-- Input para la fecha de inicio -->
            <div class="form-floating mb-3" style="width: 20vw;">
                <input
                    type="date"
                    class="form-control"
                    name="formId1"
                    id="formId1"
                    placeholder=""
                />
                <label for="formId1">Fecha de inicio</label>
            </div>
            <!-- Input para la fecha de fin -->
            <div class="form-floating mb-3" style="width: 20vw;">
                <input
                    type="date"
                    class="form-control"
                    name="formId2"
                    id="formId2"
                    placeholder=""
                />
                <label for="formId2">Fecha de fin</label>
            </div>
            <!-- Boton para enviar -->
            <button
                type="submit"
                class="btn btn-primary"
            >
                Enviar
            </button>
            
            </form>

            </div>
        </main>
        <footer>
            <!--  Footer  -->
            <div class="container-fluid bg-dark text-light d-flex align-items-center justify-content-center fixed-bottom" style="height:10vh">
                
            </div>
        </footer>
        </div>
        <!-- Bootstrap JavaScript Libraries -->
        <script
            src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js"
            integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r"
            crossorigin="anonymous"
        ></script>

        <script
            src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js"
            integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+"
            crossorigin="anonymous"
        ></script>
    </body>
</html>
