<?php
$so = scws_new();
$so->set_charset('gbk');
//$so->set_dict('C://Program Files//scws//etc//dict.utf8.xdb');
$so->set_rule('C://Program Files//scws//etc//rules.utf8.ini');
// 这里没有调用 set_dict 和 set_rule 系统会自动试调用 ini 中指定路径下的词典和规则文件
$so->send_text("我是一个中国人,我会C++语言,我也有很多T恤衣服");
while ($tmp = $so->get_result())
{
print_r($tmp);
}
$so->close();
?>