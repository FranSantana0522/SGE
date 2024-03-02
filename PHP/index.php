<!doctype html>
<html lang="en">
    <head>
        <title>Title</title>
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
            <!-- place navbar here -->
            <div class="container-fluid bg-dark text-light d-flex align-items-center justify-content-center" style="height:10vh">
                Formulario de ventas
            </div>
        </header>
        <main>
            <div class="bg-warning d-flex align-items-center justify-content-center shadow-lg" style="height:80vh">

            <form action="listadoVentas.php" method="post" class="mt-3">
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
            <button
                type="submit"
                class="btn btn-primary"
            >
                Submit
            </button>
            
            </form>

            </div>
        </main>
        <footer>
            <!-- place footer here -->
            <div class="container-fluid bg-dark text-light d-flex align-items-center justify-content-center fixed-bottom" style="height:10vh">
                footer
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
