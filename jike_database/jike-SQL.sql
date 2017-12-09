use MISA;

create table misa_jkuser(
   id bigint(20) NOT NULL AUTO_INCREMENT,
   username varchar(200) NOT NULL COMMENT '用户名',
   password varchar(200) NOT NULL COMMENT '密码',
   email varchar(200) NOT NULL COMMENT '邮箱',
   phone varchar(200) NOT NULL COMMENT '电话',
   credit bigint COMMENT '信用积分',
   PRIMARY KEY (id)
   )ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户表';

create table misa_jkmooc(
   id bigint(20) NOT NULL AUTO_INCREMENT,
   name varchar(200) NOT NULL COMMENT '资料标题',
   school varchar(200) COMMENT '学校',
   typeID varchar(100) NOT NULL COMMENT '类型',
   source varchar(200) COMMENT '来源网站',
   content varchar(800) COMMENT '内容简介',
   link varchar(200) COMMENT '链接',
   uploader varchar(200) COMMENT '上传者姓名',
   uploadtime Date COMMENT '上传时间',
   clicktime bigint COMMENT '下载次数',
   PRIMARY KEY (id)
   )ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='慕课资料表';

create table misa_jkother(
   id bigint(20) NOT NULL AUTO_INCREMENT,
   name varchar(200) NOT NULL COMMENT '资料标题',
   typeID varchar(100) NOT NULL COMMENT '类型',
   content varchar(800) COMMENT '内容简介',
   link varchar(200) COMMENT '链接',
   fileAddress varchar(300) COMMENT '文件URL地址',
   uploader varchar(200) COMMENT '上传者姓名',
   uploadtime Date COMMENT '上传时间',
   clicktime bigint COMMENT '下载次数',
   PRIMARY KEY (id)
   )ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='其他资料表';


create table misa_jkinterest(
   id bigint(20) NOT NULL AUTO_INCREMENT,
   name varchar(200) NOT NULL COMMENT '用户名',
   interest varchar(200) NOT NULL COMMENT '兴趣',
   interesttype bigint NOT NULL COMMENT '兴趣类别',
   PRIMARY KEY (id),
   )ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户兴趣表';

create table misa_jkcollection(
   id bigint(20) NOT NULL AUTO_INCREMENT,
   name varchar(200) NOT NULL COMMENT '用户名',
   resourceID bigint(20) NOT NULL COMMENT '资源编号',
   resourcetype bigint NOT NULL COMMENT '资源类别',
   PRIMARY KEY (id),
   )ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户收藏表';