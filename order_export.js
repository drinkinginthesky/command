const fs = require('fs');
const data = require('./data.json');
const json2csv = require('json2csv');
const Iconv = require('iconv').Iconv;

const iconv = new Iconv('UTF-8', 'GBK');
const fields = [{
    label: '商品ID',
    value: 'goodsId'
}, {
    label: '价格',
    value: 'price'
}, {
    label: '用户名',
    value: 'userName'
}, {
    label: '电话',
    value: 'userPhone'
}, {
    label: '收货地址',
    value: 'userAddress'
}];
const csv = json2csv({data: data, fields: fields});

// 转码
const buf = iconv.convert(csv);

fs.writeFile('数据.csv', buf, (err) => {
    if (err) throw err;
    console.log('保存成功!');
});
