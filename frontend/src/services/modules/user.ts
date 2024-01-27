import Request from '../requests/index';

export function login_md(user:login_user){
    return Request.post({
        url: '/login',
        data: {
            'username': user.username,
            'password': user.password,
        }
    });
}
const get_user_info = ()=>{
    return Request.get({
        url: '/info'
    });
}
export async function user_info_md(){
   try{
        let data = await get_user_info();
    if (data.code === 200){
        return {
            username: data.data.username,
            nickname: data.data.nickname,
            email: data.data.email,
            phone: data.data.phone,
            avatar: data.data.avatar,
            role: data.data.role,
        }
    }
    else return null;
   }
    catch (e) {
         return null;
    }
}
export function statistics_md(){
    return Request.get({
        url: '/statistics'
    });
}
