use JIKE;

create table jike_user(
   id bigint(20) NOT NULL AUTO_INCREMENT
   username varchar(200) NOT NULL COMMENT '用户名',
   password varchar(200) NOT NULL COMMENT '密码',
   email varchar(200) NOT NULL COMMENT '邮箱',
   phone varchar(200) NOT NULL COMMENT '电话',
   credit bigint COMMENT '信用积分'
   PRIMARY KEY (id),
   )ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户表';

create table jike_mooc(
   id bigint(20) NOT NULL AUTO_INCREMENT,
   name varchar(200) NOT NULL COMMENT '资料标题',
   school varchar(200) COMMENT '学校',
   source varchar(200) COMMENT '来源网站',
   content varchar(800) COMMENT '内容简介',
   link varchar(200) COMMENT '链接',
   uploader varchar(200) COMMENT '上传者姓名',
   uploadtime Date COMMENT '上传时间',
   clicktime bigint COMMENT '下载次数',
   PRIMARY KEY (id),
   )ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='慕课资料表';

create table jike_other(
   id bigint(20) NOT NULL AUTO_INCREMENT,
   name varchar(200) NOT NULL COMMENT '资料标题',
   content varchar(800) COMMENT '内容简介',
   link varchar(200) COMMENT '链接',
   file varchar(300) COMMENT '文件URL地址',
   uploader varchar(200) COMMENT '上传者姓名',
   uploadtime Date COMMENT '上传时间',
   clicktime bigint COMMENT '下载次数',
   PRIMARY KEY (id),
   )ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='其他资料表';


create table jike_interest(
   id bigint(20) NOT NULL AUTO_INCREMENT,
   userid bigint(20) NOT NULL COMMENT '用户ID',
   interest varchar(200) NOT NULL COMMENT '兴趣',
   interesttype bigint NOT NULL COMMENT '兴趣类别',
   PRIMARY KEY (id),
   )ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户兴趣表';

create table jike_collection(
   id bigint(20) NOT NULL AUTO_INCREMENT,
   userid varchar(100) NOT NULL COMMENT '项目名称',
   resourceID bigint(20) NOT NULL COMMENT '资源编号',
   resourcetype bigint NOT NULL COMMENT '资源类别',
   PRIMARY KEY (id),
   CONSTRAINT misa_4 FOREIGN KEY (uploader) REFERENCES Memeber(id)
   )ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户收藏表';