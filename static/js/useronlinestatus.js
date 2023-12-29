var ws = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/'
    + 'onlinestatus'
    + '/'
);

ws.onopen = function (e) {
    console.log('status connected')
};

ws.onclose = function () {
    console.log('status disconnected');
};