'use strict';
var ruta='http://'+document.location.hostname+':'+document.location.port;
var Personas = httpVueLoader(ruta+'/static/vue/js/persona/personas.vue')
var Personas_Create = httpVueLoader(ruta+'/static/vue/js/persona/personas_create.vue')
var Personas_Editar = httpVueLoader(ruta+'/static/vue/js/persona/personas_editar.vue')
var Solicitudes = httpVueLoader(ruta+'/static/vue/js/solicitud/solicitud.vue')
var Solicitud_Create = httpVueLoader(ruta+'/static/vue/js/solicitud/solicitud_create.vue')
var Solicitud_Editar = httpVueLoader(ruta+'/static/vue/js/solicitud/solicitud_editar.vue')


/* Router and App setup: */
var routes = [{
  path: '/personas',
  name: 'Personas',
  component: Personas
},
{
  path: '/personas_create',
  name: 'Personas_Create',
  component: Personas_Create
},
{
  path: '/personas_editar/:id_persona',
  name: 'Personas_Editar',
  component: Personas_Editar
},
{
  path: '/solicitudes',
  name: 'Solicitudes',
  component: Solicitudes
},
{
  path: '/solicitud_create',
  name: 'Solicitud_Create',
  component: Solicitud_Create
},
{
  path: '/solicitud_editar/:id_solicitud',
  name: 'Solicitud_Editar',
  component: Solicitud_Editar
},
];

var router = new VueRouter({
  routes: routes,
});

var app = new Vue({
  router: router
}).$mount('#app');
