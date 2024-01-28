import Request from '../requests/index';

export function getOption_md(key: string) {
    return Request.post({
        url: '/option',
        data: {
            'key': key
        }
    });
}

export function updateOption_md(key: string, value: string) {
    return Request.post({
        url: '/option/update',
        data: {
            'key': key,
            'value': value
        }
    });
}
