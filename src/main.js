import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import store from './store'
import VueResource from 'vue-resource'

import './filters'
import 'roboto-fontface/css/roboto/roboto-fontface.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'

Vue.use(VueResource)

Vue.config.productionTip = false
// Vue.http.options.emulateJSON = true;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
