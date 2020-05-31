<template>
  <div>  
    <div class="panel panel-primary" style="margin-left: 200px;margin-right: 200px">
                <div class="panel-heading"><h3 class="panel-title"><i class="fa fa-edit"></i> Editar Solicitud</h3></div>
                    <div class="panel-body">
                     <form role="form" class="form-horizontal" method="PUT" v-on:submit.prevent="editar">
                         
                        <div class="form-body">
                           <div class="form-group">
                             <label class="col-md-3 control-label">Persona</label>
                             <div class="col-md-8">
                             <select id="miSelect" v-model="solicitud.persona" data-placeholder="Seleccione persona" style="width:100% !important;margin-left: 0px !important">
                             <option v-for="opt in options" v-bind:value="opt.id">
                             {{ opt.name }} 
                             </option>
                             </select>                              
                             </div>                             
                           </div>
                           <div class="form-group">
                             <label class="col-md-3 control-label" >Número de mascotas</label>
                             <div class="col-md-8">
                             <input type="text" class="form-control" id="numero_mascotas" name="numero_mascotas"v-model="solicitud.numero_mascotas">
                             <span v-for="error in errors.numero_mascotas" class="text-danger"><i class="fa fa-warning"></i> {{ error }}</span>   
                             </div>
                           </div>
                           <div class="form-group">
                             <label class="col-md-3 control-label">Razones</label>
                             <div class="col-md-8">
                             <input type="text" class="form-control" id="razones" name="razones" v-model="solicitud.razones">
                             <span v-for="error in errors.razones" class="text-danger"><i class="fa fa-warning"></i> {{ error }}</span>  
                             </div>
                           </div>                            
                        </div>
                        <div class="form-actions fluid">   
                           <div class="col-md-offset-7 col-md-4">
                              <router-link :to="{ name: 'Solicitudes'}" class="btn btn-default"> <i class="fa fa-list"></i> Solicitudes</router-link>                      
                              <button type="submit" class="btn btn-primary"><i class="fa fa-check"></i> Actualizar</button> 
                           </div>                           
                        </div>
                     </form>
                    </div>
    </div>

  </div>
</template>

<script>
module.exports = {

  created: function(){
       this.get_solicitud();       
  },
  data(){
   return{
    solicitud:{
      persona:'',
      numero_mascotas:'',
      razones:'',
    },
    errors:[],
    id_solicitud:this.$route.params.id_solicitud,
    options: []
  }   
  },
  methods: {
    editar:function(){

    var url =`http://localhost:8000/persona/solicitud_actualizar/${this.id_solicitud}/`;
        axios.put(url,this.solicitud).then(response => {      
        this.solicitud.persona=response.data.solicitud.persona;
        this.solicitud.numero_mascotas=response.data.solicitud.numero_mascotas;
        this.solicitud.razones=response.data.solicitud.razones;
        //console.log(response.data.persona) 
        this.errors=[];
        toastr.success('Operación exitosa.' );
    }).catch(error => {
        this.errors=error.response.data.error;
        toastr.error('Existen errores.');
    });

    },

    cargar_personas:function(){
        var url ='http://localhost:8000/persona/personas_select2/';
        axios.get(url).then(response => {  
        this.options=response.data;
    }).catch(error => {
        this.errors=error.response.data.error;
        toastr.error('Existen errores.');
    });
    },

    get_solicitud:function(){

    var url =`http://localhost:8000/persona/solicitud_detalles/${this.id_solicitud}`;
    
    axios.get(url).then(response => {

        this.solicitud.persona=response.data.solicitud.persona;
        this.solicitud.numero_mascotas=response.data.solicitud.numero_mascotas;
        this.solicitud.razones=response.data.solicitud.razones;
        this.cargar_personas(); 
    }).catch(error => {
         
         
    });

    },

  },
      mounted(){

        var vm = this;        
        $('#miSelect').select2();
        $('#miSelect').change(function (){
          vm.solicitud.persona =$("#miSelect option:selected").val();                  
        });

    }
}
</script>
<style>
.form-group .select2-container .select2-choice {
    width: 100%;
    margin-top: 0px;
    margin-left:0px;
}
</style>