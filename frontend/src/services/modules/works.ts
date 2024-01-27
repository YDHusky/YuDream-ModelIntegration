import Request from '../requests/index';

export function get_works_md(){
    return Request.post({
        url: '/out/user'
    });
}

export function save_works_md(work_name:string, url:string){

    return Request.post({
        url: '/out/save',
        data: {
            'work_name': work_name,
            'url': url,
        }
    });
}
export function delete_works_md(id:any){
    return Request.post({
        url: '/out/delete',
        data: {
            'id': id,
        }
    });
}
export function update_works_md(id:any, work_name:string){
    return Request.post({
        url: '/out/edit',
        data: {
            'id': id,
            'work_name': work_name,
        }
    });
}