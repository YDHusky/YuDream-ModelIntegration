import Request from '../requests/index';

export function login_md(user: login_user) {
    return Request.post({
        url: '/login',
        data: {
            'username': user.username,
            'password': user.password,
        }
    });
}

const get_user_info = () => {
    return Request.get({
        url: '/info'
    });
}

export async function user_info_md() {
    try {
        let data = await get_user_info();
        if (data.code === 200) {
            return {
                username: data.data.username,
                nickname: data.data.nickname,
                email: data.data.email,
                phone: data.data.phone,
                avatar: data.data.avatar,
                role: data.data.role,
            }
        } else return null;
    } catch (e) {
        return null;
    }
}

export function statistics_md() {
    return Request.get({
        url: '/statistics'
    });
}

export function update_user_info_md(user: user_info) {
    return Request.post({
        url: '/info/update',
        data: {
            'nickname': user.nickname,
            'email': user.email,
            'phone': user.phone,
        }
    });
}

export function update_user_password_md(user: password_info) {
    return Request.post({
        url: '/info/update/password',
        data: {
            'old_password': user.old_password,
            'new_password': user.new_password,
        }
    });
}

export function register_md(user: any) {
    return Request.post({
        url: '/add',
        data: {
            'username': user.username,
            'password': user.password,
            'nickname': user.nickname,
            'phone': user.phone,
        }
    });
}

export function get_all_users_md() {
    return Request.get({
        url: '/list'
    });
}

export function get_user_by_username_md(username: string) {
    console.log(username)
    return Request.post({
        url: '/info/username',
        data: {
            'username': username
        }
    });
}

export function update_user_by_admin(user:any){
    return Request.post({
        url: '/info/admin/update',
        data: {
            'username': user.username,
            'nickname': user.nickname,
            'email': user.email,
            'phone': user.phone,
            'role': user.role,
        }
    });
}

export function update_user_password_by_admin(user:any){
    return Request.post({
        url: '/info/admin/password',
        data: {
            'username': user.username,
            'password': user.password,
        }
    });
}

export function delete_user_by_admin(username:string){
    return Request.post({
        url: '/info/delete',
        data: {
            'username': username
        }
    });
}

export function add_user_by_admin(user:any){
    return Request.post({
        url: '/info/admin/add',
        data: {
            'username': user.username,
            'password': user.password,
            'nickname': user.nickname,
            'phone': user.phone,
            'role': user.role,
            'email': user.email,
        }
    });
}

export function get_statistics_admin_md(){
    return Request.get({
        url: '/statistics/admin'
    });
}