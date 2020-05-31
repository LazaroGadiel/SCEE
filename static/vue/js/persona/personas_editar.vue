<template>
  <div>  
<div class="panel panel-primary" style="margin-left: 200px;margin-right: 200px">
                <div class="panel-heading"><h3 class="panel-title"><i class="fa fa-edit"></i> Editar Persona</h3></div>
                    <div class="panel-body">
                     <form role="form" class="form-horizontal" method="POST" v-on:submit.prevent="editar">
                        
                        <div class="form-body">

                           <div class="form-group">
                             <label class="col-md-3 control-label">Nombre</label>
                             <div class="col-md-8">
                             <input type="text" class="form-control" id="name" name="name" v-model="persona.name">
                             <span v-for="error in errors.name" class="text-danger">{{ error }}</span>  
                             </div>
                           </div>
                           <div class="form-group">
                             <label class="col-md-3 control-label" >Plaza</label>
                             <div class="col-md-8">
                             <input type="text" class="form-control" id="plaza" name="plaza" v-model="persona.plaza">
                             <span v-for="error in errors.plaza" class="text-danger">{{ error }}</span>   
                             </div>
                           </div>
                           <div class="form-group">
                             <label class="col-md-3 control-label">Fijo</label>
                             <div class="col-md-8">
                             <input type="text" class="form-control" id="fijo" name="fijo" v-model="persona.fijo">
                             <span v-for="error in errors.fijo" class="text-danger">{{ error }}</span>  
                             </div>
                           </div>
                           <div class="form-group">
                             <label class="col-md-3 control-label">Celular</label>
                             <div class="col-md-8">
                             <input type="text" class="form-control" id="celular" name="celular" v-model="persona.celular">
                             <span v-for="error in errors.celular" class="text-danger">{{ error }}</span>  
                             </div>
                           </div>
                           <div class="form-group">
                             <label class="col-md-3 control-label">Cargo</label>
                             <div class="col-md-8">
                             <input type="text" class="form-control" id="cargo" name="cargo" v-model="persona.cargo">
                             <span v-for="error in errors.cargo" class="text-danger">{{ error }}</span>  
                             </div>
                           </div>
                           <div class="form-group">
                             <label class="col-md-3 control-label">Unidad </label>
                             <div class="col-md-8">
                             <input type="text" class="form-control" id="uo" name="uo" v-model="persona.uo">
                             <span v-for="error in errors.uo" class="text-danger">{{ error }}</span>  
                             </div>
                           </div>
                        </div>
                        <div class="form-actions fluid">   
                           <div class="col-md-offset-9 col-md-1">                      
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
       this.get_persona();
  },
  data(){
   return{
    persona:{
      name:'',
      plaza:'',
      fijo:'',
      celular:'',
      cargo:'',
      uo:''
    },
    errors:[],
    id_persona:this.$route.params.id_persona
  }   
  },
  methods: {
    editar:function(){

    var url =`http://`+document.location.hostname+':'+document.location.port+`/persona/actualizar/${this.id_persona}/`;
        axios.put(url,this.persona).then(response => {      
        this.persona.name=response.data.persona.name;
        this.persona.plaza=response.data.persona.plaza;
        this.persona.fijo=response.data.persona.fijo;
        this.persona.cargo=response.data.persona.cargo;
        this.persona.celular=response.data.persona.celular;
        this.persona.uo=response.data.persona.uo;
        //console.log(response.data.persona) 
        this.errors=[];
        toastr.success('Operación exitosa.' );
    }).catch(error => {
        this.errors=error.response.data.error;
        toastr.error('Existen errores.');
    });

    },
    limpiar:function(){
      this.persona.name='';
      this.persona.plaza='';
      this.persona.fijo='';
      this.persona.cargo='';
      this.persona.celular='';
      this.persona.uo='';    
    },

    get_persona:function(){
    var url =`http://`+document.location.hostname+':'+document.location.port+`/persona/detalles/${this.id_persona}`;
        axios.get(url).then(response => {  
        this.persona.name=response.data.persona.name;
        this.persona.plaza=response.data.persona.plaza;
        this.persona.fijo=response.data.persona.fijo;
        this.persona.cargo=response.data.persona.cargo;
        this.persona.celular=response.data.persona.celular;
        this.persona.uo=response.data.persona.uo;  
         
    }).catch(error => {
         
         
    });

    },

  }
}
