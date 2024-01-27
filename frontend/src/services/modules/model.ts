import Request from '../requests/index';

export function getModelList_md(){
    return Request.get({
        url: '/model/list',
    });
}