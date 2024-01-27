import Request from '../requests/index';

export function getOption_md(key: string) {
    return Request.post({
        url: '/option',
        data: {
            'key': key
        }
    });
}
