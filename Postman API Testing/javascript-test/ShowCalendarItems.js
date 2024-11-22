pm.test("Status is 200", function () {
    pm.response.to.have.status(200);
});

let jsonResponse;
try {
    jsonResponse = pm.response.json();

    pm.test("El campo 'success' es verdadero", function () {
        pm.expect(jsonResponse.success).to.be.true;
    });

} catch (e) {
    pm.test("La respuesta no es un JSON válido", function () {
        pm.expect.fail("Error al analizar la respuesta JSON: " + e.message);
    });
}
