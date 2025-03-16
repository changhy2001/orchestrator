import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '@/views/HomePage.vue'; // your Home component
import AboutPage from '@/views/AboutPage.vue';
import LoginPage from '@/views/LoginPage.vue';
import RegisterPage from '@/views/RegisterPage.vue';
import AppHomePage from '@/views/AppHomePage.vue';
import UserMeta from '@/views/searchapp/UserMeta.vue';
import UserMetaDetail from '@/views/searchapp/UserMetaDetail.vue';


const routes = [
  { path: '/', name: 'Home', component: HomePage },
  { path: '/about', name: 'About', component: AboutPage },
  { path: '/login', name: 'Login', component: LoginPage },
  { path: '/register', name: 'Register', component: RegisterPage },
  { path: '/searchapp', name: 'SearchApp', component: AppHomePage },
  { path: '/searchapp/usermeta', name: 'UserMeta', component: UserMeta},
  { path: '/searchapp/usermeta/:pk', name: 'UserMetaDetail', component: UserMetaDetail},
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
