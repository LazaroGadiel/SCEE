<template>
  <div>  
<div class="panel panel-primary" style="margin-left: 200px;margin-right: 200px">
                <div class="panel-heading"><h3 class="panel-title"><i class="fa fa-plus"></i> Adicionar Persona</h3></div>
                    <div class="panel-body">
                     <form role="form" class="form-horizontal" method="POST" v-on:submit.prevent="crear">
                         
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
  }   
  },
  methods: {
    crear:function(){

    var url ='http://'+document.location.hostname+':'+document.location.port+'persona/nuevo/';
        axios.post(url,this.persona).then(response => {
        this.limpiar();
        this.errors=[];
        toastr.success('Operación exitosa.'); 
        
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
    }
  }
}
