create database QLVT;
Go

USE QLVT;

CREATE TABLE VATTU(
	MaVT char(16) not null primary key,
	TenVT nvarchar(128),
	LoaiVT nvarchar(64)
)
