pm.test("Status is 201", function () {
    pm.response.to.have.status(201);
});

let jsonResponse;
try {
    jsonResponse = pm.response.json();

    pm.test("El token de sesión existe", function () {
        pm.expect(jsonResponse).to.have.property("token");
        pm.expect(jsonResponse.token).to.be.a("string").that.is.not.empty;
    });

    pm.test("El token es de tipo Bearer", function () {
        pm.expect(jsonResponse).to.have.property("token_type");
        pm.expect(jsonResponse.token_type).to.be.a("string").that.includes('Bearer');
    });

    if (jsonResponse.token) {
        console.log("Token:", jsonResponse.token);
    }

    pm.test("El campo 'redirect_to' existe y tiene un valor válido", function () {
        pm.expect(jsonResponse).to.have.property("redirect_to");
        pm.expect(jsonResponse.redirect_to).to.be.a("string").that.includes("http://127.0.0.1:8000/home");
    });

    if (jsonResponse.redirect_to) {
        console.log("Redirect to:", jsonResponse.redirect_to);
    }

    pm.test("El campo 'success' es verdadero", function () {
        pm.expect(jsonResponse.success).to.be.true;
    });

} catch (e) {
    pm.test("La respuesta no es un JSON válido", function () {
        pm.expect.fail("Error al analizar la respuesta JSON: " + e.message);
    });
}
