<template>
  <div>  
    <div class="panel panel-primary" style="margin-left: 200px;margin-right: 200px">
                <div class="panel-heading"><h3 class="panel-title"><i class="fa fa-plus"></i> Adicionar Solicitud</h3></div>
                    <div class="panel-body">
                     <form role="form" class="form-horizontal" method="POST" v-on:submit.prevent="crear">
                         
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
                             <span v-for="error in errors.numero_mascotas" class="text-danger"> <i class="fa fa-warning"></i> {{ error }}</span>   
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
                              <button type="submit" class="btn btn-primary"><i class="fa fa-check"></i> Adicionar</button> 
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
       this.cargar_personas();
  },
  data(){
   return{
    solicitud:{
      persona:'',
      numero_mascotas:'',
      razones:'',
    },
    errors:[],
    options: []
  }   
  },
  methods: {
    crear:function(){
    var url ='http://localhost:8000/persona/solicitud_crear/';      
        
        axios.post(url,this.solicitud).then(response => {
        this.limpiar();
        this.errors=[];
        toastr.success('Operación exitosa.' );         
        }).catch(error => {
        this.errors=error.response.data.error;
        toastr.error('Existen errores.');
         });

    },
    limpiar:function(){
      this.solicitud.numero_mascotas='';
      this.solicitud.razones='';
      //this.solicitud.persona='';   
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
    onChange:function(){
      alert('cambio');
    }
    
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
