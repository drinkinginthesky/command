const fs = require('fs');
const data = require('./vip.json');
const json2csv = require('json2csv');
const Iconv = require('iconv').Iconv;
const iconv = new Iconv('UTF-8', 'GBK');
const fields = [
{
    label: '用户ID',
    value: 'userId.$oid'
}
, {
    label: '用户名',
    value: 'nickname'
}
, {
    label: '登录手机号',
    value: 'loginphone'
}
, {
    label: '支付时间',
    value: 'updateAt'
}
, {
    label: '身份证',
    value: 'id'
}
, {
    label: '电话',
    value: 'phone'
}
, {
    label: '收货地址',
    value: 'address'
}
, {
    label: '微博ID',
    value: 'weiboName'
}
, {
    label: '工作',
    value: 'job'
}
, {
    label: '教育',
    value: 'education'
}
];
const csv = json2csv({data: data, fields: fields});

// 转码
// const buf = iconv.convert(csv);

fs.writeFile('./data/VIP订单.csv', csv, (err) => {
    if (err) throw err;
    console.log('保存成功!');
});
