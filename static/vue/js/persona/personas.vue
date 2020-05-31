<template>
<div>
 <div class="row" style="margin-left: 0px;margin-right: 0px">
        <div class="col-md-12" >
          <!-- BEGIN EXAMPLE TABLE PORTLET-->
          <div class="panel panel-primary">
        <div class="panel-heading"><h3 class="panel-title"><i class="fa fa-list"></i> Listado de personas</h3>
            </div>
            <div class="panel-body">
            <div class="col-md-12 hidden-print">
            <div class="btn-group" data-toggle="buttons" style="margin-bottom: 10px">
                  <label class="btn btn-sm blue"  v-on:click.prevent="adicionar()">
                  <input type="radio" class="toggle"><i class="fa fa-plus"></i> Adicionar</label>
              </div>  
              <div class="btn-group pull-right" data-toggle="buttons" style="margin-bottom: 10px">
                  <label class="btn btn-sm default"  v-on:click.prevent="listar_personas()">
                  <input type="radio" class="toggle"><i class="fa fa-refresh"></i></label>
                  <label class="btn btn-sm purple" v-on:click="javascript:window.print()">
                  <input type="radio" class="toggle"><i class="fa fa-print"></i></label>
                  <label class="btn btn-sm red" v-on:click.prevent="Export()">
                  <input type="radio" class="toggle"><i class="fa fa-file-pdf-o"></i></label>
                  <label class="btn btn-sm green" v-on:click.prevent="exportar()">
                  <input type="radio" class="toggle"><i class="fa fa-file-excel-o"></i></label>
              </div>
            </div>   
            <div class="col-md-12">               
              <table class="table table-striped table-bordered table-hover" id="sample_1">
              <thead>
              <tr>
                <!--
                <th class="table-checkbox">
                  <input type="checkbox" class="group-checkable" data-set="#sample_1 .checkboxes"/>
                </th>
                 -->
                <th>PK</th> 
                <th>Nombre</th>
                <th>Plaza</th>
                <th>Fijo</th>
                <th>Celular</th>
                <th>Cargo</th>
                <th>Unidad</th>
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

      this.listar_personas();

  },
  data(){
   return{
    personas:[],
      
  }   
  },
  methods: {
    listar_personas:function(){
      waitingDialog.show('Cargando...',{dialogSize: 'sm', progressType: 'primary'});
      var url='http://'+document.location.hostname+':'+document.location.port+'/persona/listado/';
      axios.get(url).then((response) => { 
      this.personas = response.data;
      this.configurar_tabla();      
      }).catch((error)=>{
         console.log(error)
      });
      waitingDialog.hide('Cargando...',{dialogSize: 'sm', progressType: 'primary'});

    },
    eliminar_persona: function(persona) {
     var url ='http://'+document.location.hostname+':'+document.location.port+'/persona/eliminar/'+localStorage.getItem('persona_pk');
         axios.delete(url).then(response => {
         this.listar_personas();          
         $('#delete').modal('hide');
         toastr.success('Eliminado correctamente');                   
        });
    },
    adicionar: function() {
     window.location='#/personas_create';
    },
    Export:function() {
            html2canvas(document.getElementById('sample_1'),{
                onrendered: function (canvas) {
                    var data = canvas.toDataURL();
                    var docDefinition = {
                        content: [{
                            image: data,
                            width: 500
                        }]
                    };
                    pdfMake.createPdf(docDefinition).download("Reporte.pdf");
                }
            });
    },
    exportar:function(){
        $("#sample_1").table2excel({
           filename: "Personas.xls"
        });
    },    
    configurar_tabla:function(){   
     var table= $('#sample_1').dataTable({
      "bDestroy":true,
      "data":this.personas,
      "columnDefs": [
                 {
                  "targets": [ 0 ],
                  "visible": false,
                  "searchable": false, 
                    }
                ],
      "columns": [
            {"data" : "pk"},
            { "data": "fields.name" },
            { "data": "fields.plaza" },
            { "data": "fields.fijo" },
            { "data": "fields.celular" },
            { "data": "fields.cargo" },
            { "data": "fields.uo" },
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
           //alert(data.pk)
           localStorage.setItem('persona_pk',data.pk);
           $('#nombre').text(data.fields.name)
           $('#delete').modal('show');
           $('#editar').remove();     
        } );
        table.on( 'click', 'tbody tr .btn-warning', function () {
        tablee=$('#sample_1').DataTable(); 
        var data = tablee.row( $(this).parents('tr') ).data();
            window.location='#/personas_editar/'+data.pk   
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
     
    },

  updated() {    
 
  }  
}
</script>

