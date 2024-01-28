import Request from '../requests/index';

export function getModelList_md(){
    return Request.get({
        url: '/model/list',
    });
}

export function editModel_md(data: any){
    console.log(data)
    return Request.post({
        url: '/model/edit',
        data: {
            'name': data.name,
            'displayName': data.displayName,
            'description': data.description,
            'version': data.version,
            'author': data.author,
        }
    });
}