$(function(){
    //Zona segura de ejecucion
    console.log("hola, estoy en el formulario persona");
    //tener en cuenta agregar async a la funcion cuando usamos axios
    $('#btncrear').on('click', async function(){
        //recuperar los datos del formulario
        const nombres = $('#txtnombres').val();
        const apellidos = $('#txtapellidos').val();
        const ci = $('#txtci').val();
        const direccion = $('#txtdireccion').val();
        //diferetes formas de concatenar cadenas en JavaScrpit
        console.log('nombres = ' + nombres);
        console.log("apellidos = " + apellidos);
        console.log(`cedula ${ci}`);
        console.log(`direcion ${direccion}`);

        if(!nombres.trim()) {
            Swal.fire({
                title: "Error",
                text: "Nombre invalida",
                icon: "error"
            });
            return;
        }
        if(!apellidos.trim()) {
            Swal.fire({
                title: "Error",
                text: "Apellido invalida",
                icon: "error"
            });
            return;
        }
        if(!ci.trim()) {
            Swal.fire({
                title: "Error",
                text: "CI invalido",
                icon: "error"
            });
            return;
        }
        if(!direccion.trim()) {
            Swal.fire({
                title: "Error",
                text: "Direcion invalido",
                icon: "error"
            });
        }
        //Json -- Javascript object notation
        const persona = {
            nombres: nombres,
            apellidos: apellidos,
            cedula: ci,
            direccion: direccion
        }
        console.log(persona);
        try{
            const guardado = await axios.post('/save-persona', persona);
            console.log(guardado);
            Swal.fire({
                title: "Exitoso",
                text: "Guardando Formulario",
                icon: "success"
            });
        } catch (error){
            console.error(error);
        }
    });
});