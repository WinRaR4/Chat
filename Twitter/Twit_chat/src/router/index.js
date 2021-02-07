import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Login from '@/components/Login'
import Registrate from '@/components/Registrate'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '',
      name: 'home',
      component: Home
    },
    {
      path: '/log',
      name: 'login',
      component: Login
    },
    {
      path: '/reg',
      name: 'register',
      component: Registrate
    },
    {
      path: '/dial',
      name: 'dialog',
      component: Registrate
    }
  ]
})
