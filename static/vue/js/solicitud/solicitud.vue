<template>
<div>
 <div class="row" style="margin-left: 0px;margin-right: 0px">
        <div class="col-md-12" >
          <!-- BEGIN EXAMPLE TABLE PORTLET-->
          <div class="panel panel-primary">
            <div class="panel-heading"><h3 class="panel-title"><i class="fa fa-list"></i> Listado de solicitudes</h3>
             <div class="clearfix pull-right" style="margin-top:-18px">
               
              <a class="icon-btn" title="Actualizar" data-rel="icon-btn" href="#" v-on:click.prevent="listar()"><i class="fa fa-refresh"></i></a>
             </div>
            </div>
            <div class="panel-body">
            <div class="col-md-12">  
              <table class="table table-striped table-bordered table-hover" id="sample_1">
              <thead>
              <tr>
                <!--
                <th class="table-checkbox">
                  <input type="checkbox" class="group-checkable" data-set="#sample_1 .checkboxes"/>
                </th>
                 -->
                <th>ID</th> 
                <th>Nombre</th>
                <th>Mascotas</th>
                <th>Razones</th>
                <th>Acciones</th>
                
              </tr>
              </thead>
               
              </table>
             </div> 
            </div>
          </div>
          <!-- END EXAMPLE TABLE PORTLET-->
        </div>
  </div>

<form method="POST" v-on:submit.prevent="eliminar_persona()">
<div class="modal fade" id="delete">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal">
                    <span>×</span>
                </button>
                <h4>Opciones disponibles</h4>
            </div>
            <div class="modal-body">
                <label>Información de la persona</label>
               <p>Nombre: </p> <p id="nombre"></p>
             </div>
            <div class="modal-footer">
               
              <input type="submit" class="btn btn-danger" value="Confirmar">
            </div>
        </div>
    </div>
</div>
</form>
</div>
   
</template>
 
<script>
module.exports = {

  created: function(){

      this.listar();

  },
  data(){
   return{
    solicitudes:[],
      
  }   
  },
  methods: {
    listar:function(){
      waitingDialog.show('Cargando...',{dialogSize: 'sm', progressType: 'primary'});
      var url='http://localhost:8000/persona/listado_solicitud/';
      axios.get(url).then((response) => { 
      this.solicitudes = response.data;
      this.configurar_tabla();      
      }).catch((error)=>{
         console.log(error)
      });
      waitingDialog.hide('Cargando...',{dialogSize: 'sm', progressType: 'primary'});

    },
    eliminar_persona: function(persona) {
     var url ='http://localhost:8000/persona/solicitud_eliminar/'+localStorage.getItem('solicitud');
         axios.delete(url).then(response => {
         this.listar();          
         $('#delete').modal('hide');
         toastr.success('Eliminado correctamente');                   
        });
    },

    configurar_tabla:function(){   
     var table= $('#sample_1').dataTable({
      "bDestroy":true,
      "data":this.solicitudes,
      "columnDefs": [
                 {
                  "targets": [ 0 ],
                  "visible": false,
                  "searchable": false, 
                    }
                ],
      "columns": [
            { "data": "id"},
            { "data": "persona__name" },
            { "data": "numero_mascotas" },
            { "data": "razones" },
            { "data": null,
              "defaultContent": '<div style="text-align: center"><button class="btn btn-xs btn-warning"><i class="fa fa-edit "></i></button> <button class="btn btn-xs btn-danger"><i class="fa fa-trash-o"></i></button></div>'
             }            
        ],
      "processing": true,
      "ordering":false,
      "lengthMenu": [
                [10, 25, 50, -1],
                [10, 25, 50, "Todos"] // change per page values here
            ],
      "pageLength": 10,  
      "pagingType": "full_numbers",
      "language": {
                "search": "",
                "sSearchPlaceholder":'Buscar',
                "lengthMenu": "_MENU_",
                "paginate": {
                    "previous":"Anterior",
                    "next": "Siguiente",
                    "last": "Última",
                    "first": "Primera"
                },
                "emptyTable": "No hay registros disponibles",
                "info": "Mostrando _START_ a _END_ de _TOTAL_ registros",
                "infoEmpty": "No se encontraron resultados",
                "zeroRecords": "No se encontraron resultados"
            }         
     });

          
      var tableWrapper = jQuery('#sample_1_wrapper');

       /* table.find('.group-checkable').change(function () {
            var set = jQuery(this).attr("data-set");
            var checked = jQuery(this).is(":checked");
            jQuery(set).each(function () {
                if (checked) {
                    $(this).attr("checked", true);
                    $(this).parents('tr').addClass("active");
                     
                } else {
                    $(this).attr("checked", false);
                    $(this).parents('tr').removeClass("active");
                }
            });
            jQuery.uniform.update(set);
        });

        table.on('change', 'tbody tr .checkboxes', function () {
            $(this).parents('tr').toggleClass("active");
        });
        */
        table.on( 'click', 'tbody tr .btn-danger', function () {
        tablee=$('#sample_1').DataTable(); 
        var data = tablee.row( $(this).parents('tr') ).data();
           localStorage.setItem('solicitud',data.id);
           $('#nombre').text(data.persona__name)
           $('#delete').modal('show');
           $('#editar').remove();     
        } );
        table.on( 'click', 'tbody tr .btn-warning', function () {
        tablee=$('#sample_1').DataTable(); 
        var data = tablee.row( $(this).parents('tr') ).data();
            window.location='#/solicitud_editar/'+data.id   
        } );
        tableWrapper.find('.dataTables_length select').select2();
        tableWrapper.find('.dataTables_filter input').addClass("form-control");
        //waitingDialog.hide('Cargando...',{dialogSize: 'sm', progressType: 'primary'});
        //toastr.success('Carga exitosa.');
         $('#sample_1').css({
            'width':'auto',
        });
      
   
    } 
  },
  mounted(){     
     //this.$forceUpdate();
    },

  updated() {    
 
  }  
}
</script>

