function eliminarAlumno(tipoSolicitud, url){ 
  console.log(tipoSolicitud);
    let texto = ""

    if(tipoSolicitud == "SinRegistro"){
      texto = "Este Alumno no tiene un horario por lo que solo se eliminaran sus archivos, aun así tenga cuidado, esta acción no se puede deshacer."
    }else if(tipoSolicitud == "ConRegistro"){
      texto = "Este Alumno tiene un horario por lo que se eliminaran sus documentos, además de información de sus clases y asistencia, aun así tenga cuidado, esta acción no se puede deshacer."
    }

    console.log(texto)
    const swalWithBootstrapButtons = Swal.mixin({
      customClass: {
        confirmButton: 'btn btn-success',
        cancelButton: 'btn btn-danger'
      },
      buttonsStyling: false
    })
  
    swalWithBootstrapButtons.fire({
      title: '¿Estas Seguro?',
      text: texto,
      icon: 'warning',
      showCancelButton: true,
      confirmButtonText: '¡Si, Borrar!',
      cancelButtonText: '¡No, Cancelar!',
      confirmButtonClass: "buttonSweetalert",
      reverseButtons: true
    }).then((result) => {
      if (result.isConfirmed) {
        console.log(csrftoken)
       $.ajax({
        url:url,
        type:"POST",
        data:{"csrfmiddlewaretoken":csrftoken},
        success: function(){
           swalWithBootstrapButtons.fire(
          'Borrado!',
          'Se ha borrado este Alumno',
          'success'
        ).then(function(){
          location.reload()
        })
        },
        error: function(error){
           swalWithBootstrapButtons.fire(
          'ERROR!',
           error["mensaje"],
          'error'
        )
        },
       })
      } else if (
        /* Read more about handling dismissals below */
        result.dismiss === Swal.DismissReason.cancel
      ) {
        swalWithBootstrapButtons.fire(
          'Cancelado',
          'No se han aplicado cambios',
          'error'
        )
      }
    })

    }