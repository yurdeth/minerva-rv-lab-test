pm.test("Status is 200", function () {
    pm.response.to.have.status(200); // Verifica que la respuesta sea 200
});

// Extraer el cuerpo de la respuesta como JSON
let jsonResponse;
try {
    jsonResponse = pm.response.json();

    pm.test("El campo 'message' existe y tiene el valor esperado", function () {
        pm.expect(jsonResponse).to.have.property("message");
        pm.expect(jsonResponse.message).to.eql("Cita registrada");
    });

    pm.test("El campo 'redirect_to' existe y tiene el valor esperado", function () {
        pm.expect(jsonResponse).to.have.property("redirect_to");
        pm.expect(jsonResponse.redirect_to).to.eql("/dashboard/citas");
    });

    pm.test("El campo 'success' es verdadero", function () {
        pm.expect(jsonResponse.success).to.be.true;
    });

    // Imprimir los valores para verificar en consola
    console.log("Mensaje:", jsonResponse.message);
    console.log("Redirect to:", jsonResponse.redirect_to);
    console.log("Success:", jsonResponse.success);

} catch (e) {
    pm.test("La respuesta no es un JSON válido", function () {
        pm.expect.fail("Error al analizar la respuesta JSON: " + e.message);
    });
}
