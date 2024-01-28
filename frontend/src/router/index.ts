import {createRouter, createWebHashHistory} from 'vue-router'
import MainLayout from "@/components/layout/MainLayout.vue";
import LoginPage from "@/views/login/LoginPage.vue";
import UserLayout from "@/components/layout/UserLayout.vue";
import UserPage from "@/views/user/UserPage.vue";
import CreativeCenter from "@/views/user/CreativeCenter.vue";
import WorksPage from "@/views/user/WorksPage.vue";
import SettingPage from "@/views/user/SettingPage.vue";
import AdminPage from "@/views/admin/AdminPage.vue";
import AdminLayout from "@/components/layout/AdminLayout.vue";
import HomePage from "@/views/home/HomePage.vue";
import {user_info_md} from "@/services/modules/user";
import RegisterPage from "@/views/login/RegisterPage.vue";
import WorkAdminPage from "@/views/admin/WorkAdminPage.vue";
import UserAdminPage from "@/views/admin/UserAdminPage.vue";
import ModelInfoPage from "@/views/admin/ModelInfoPage.vue";
import AdminSetting from "@/views/admin/AdminSetting.vue";

const router = createRouter({
    history: createWebHashHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'Home',
            component: MainLayout,
            children: [
                {
                    path: '/',
                    name: 'HomePage',
                    component: HomePage
                }, {
                    path: '/login',
                    name: 'LoginPage',
                    component: LoginPage
                },
                {
                    path: '/register',
                    name: 'RegisterPage',
                    component: RegisterPage
                }
            ],
        },
        {
            path: '/user',
            name: 'User',
            meta: {
                requiresAuth: true
            },
            component: UserLayout,
            children: [
                {
                    path: '/user',
                    name: 'UserPage',
                    component: UserPage,
                },
                {
                    path: '/user/creation',
                    name: 'CreativeCenter',
                    component: CreativeCenter
                },
                {
                    path: '/user/works',
                    name: 'Works',
                    component: WorksPage
                },
                {
                    path: '/user/setting',
                    name: 'Setting',
                    component: SettingPage
                }

            ]
        },
        {
            path: '/admin',
            name: 'Admin',
            meta: {
                requiresAuth: true,
                role: 3
            },
            component: AdminLayout,
            children: [
                {
                    path: '/admin',
                    name: 'AdminPage',
                    component: AdminPage,
                }, {
                    path: '/admin/works',
                    name: 'AdminWorksPage',
                    component: WorkAdminPage
                }, {
                    path: '/admin/users',
                    name: 'AdminUsersPage',
                    component: UserAdminPage
                }, {
                    path: '/admin/model',
                    name: 'ModelInfoPage',
                    component: ModelInfoPage
                },{
                    path: '/admin/setting',
                    name: 'AdminSettingPage',
                    component: AdminSetting
                }
            ]
        }
    ]
})
router.beforeEach((to, from, next) => {
    try {
        if (!to.meta.requiresAuth) {
            next()
        } else {
            let data = user_info_md();
            if (data != null) {
                data.then((res) => {
                    if (res !== null) {
                        if (to.meta.role && to.meta.role > res.role) {
                            next({path: from.path})
                        } else next()
                    } else {
                        next({path: '/login'})
                    }
                })

            } else {
                next({path: '/login'})
            }
        }
    } catch (e) {
        next({path: '/login'})
    }
});

export function logOutLogIn() {
    sessionStorage.removeItem('token')
    router.push('/')
}

export default router
