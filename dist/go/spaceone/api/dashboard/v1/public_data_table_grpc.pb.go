// description of data table

// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.3.0
// - protoc             v3.6.1
// source: spaceone/api/dashboard/v1/public_data_table.proto

package v1

import (
	context "context"
	empty "github.com/golang/protobuf/ptypes/empty"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

const (
	PublicDataTable_Create_FullMethodName = "/spaceone.api.data_table.v1.PublicDataTable/create"
	PublicDataTable_Update_FullMethodName = "/spaceone.api.data_table.v1.PublicDataTable/update"
	PublicDataTable_Delete_FullMethodName = "/spaceone.api.data_table.v1.PublicDataTable/delete"
	PublicDataTable_Load_FullMethodName   = "/spaceone.api.data_table.v1.PublicDataTable/load"
	PublicDataTable_Get_FullMethodName    = "/spaceone.api.data_table.v1.PublicDataTable/get"
	PublicDataTable_List_FullMethodName   = "/spaceone.api.data_table.v1.PublicDataTable/list"
)

// PublicDataTableClient is the client API for PublicDataTable service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type PublicDataTableClient interface {
	Create(ctx context.Context, in *CreatePublicDataTableRequest, opts ...grpc.CallOption) (*PublicDataTableInfo, error)
	Update(ctx context.Context, in *UpdatePublicDataTableRequest, opts ...grpc.CallOption) (*PublicDataTableInfo, error)
	Delete(ctx context.Context, in *PublicDataTableRequest, opts ...grpc.CallOption) (*empty.Empty, error)
	Load(ctx context.Context, in *LoadPublicDataTableRequest, opts ...grpc.CallOption) (*PublicDataTableInfo, error)
	Get(ctx context.Context, in *PublicDataTableRequest, opts ...grpc.CallOption) (*PublicDataTableInfo, error)
	List(ctx context.Context, in *PublicDataTableQuery, opts ...grpc.CallOption) (*PublicDataTablesInfo, error)
}

type publicDataTableClient struct {
	cc grpc.ClientConnInterface
}

func NewPublicDataTableClient(cc grpc.ClientConnInterface) PublicDataTableClient {
	return &publicDataTableClient{cc}
}

func (c *publicDataTableClient) Create(ctx context.Context, in *CreatePublicDataTableRequest, opts ...grpc.CallOption) (*PublicDataTableInfo, error) {
	out := new(PublicDataTableInfo)
	err := c.cc.Invoke(ctx, PublicDataTable_Create_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *publicDataTableClient) Update(ctx context.Context, in *UpdatePublicDataTableRequest, opts ...grpc.CallOption) (*PublicDataTableInfo, error) {
	out := new(PublicDataTableInfo)
	err := c.cc.Invoke(ctx, PublicDataTable_Update_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *publicDataTableClient) Delete(ctx context.Context, in *PublicDataTableRequest, opts ...grpc.CallOption) (*empty.Empty, error) {
	out := new(empty.Empty)
	err := c.cc.Invoke(ctx, PublicDataTable_Delete_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *publicDataTableClient) Load(ctx context.Context, in *LoadPublicDataTableRequest, opts ...grpc.CallOption) (*PublicDataTableInfo, error) {
	out := new(PublicDataTableInfo)
	err := c.cc.Invoke(ctx, PublicDataTable_Load_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *publicDataTableClient) Get(ctx context.Context, in *PublicDataTableRequest, opts ...grpc.CallOption) (*PublicDataTableInfo, error) {
	out := new(PublicDataTableInfo)
	err := c.cc.Invoke(ctx, PublicDataTable_Get_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *publicDataTableClient) List(ctx context.Context, in *PublicDataTableQuery, opts ...grpc.CallOption) (*PublicDataTablesInfo, error) {
	out := new(PublicDataTablesInfo)
	err := c.cc.Invoke(ctx, PublicDataTable_List_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// PublicDataTableServer is the server API for PublicDataTable service.
// All implementations must embed UnimplementedPublicDataTableServer
// for forward compatibility
type PublicDataTableServer interface {
	Create(context.Context, *CreatePublicDataTableRequest) (*PublicDataTableInfo, error)
	Update(context.Context, *UpdatePublicDataTableRequest) (*PublicDataTableInfo, error)
	Delete(context.Context, *PublicDataTableRequest) (*empty.Empty, error)
	Load(context.Context, *LoadPublicDataTableRequest) (*PublicDataTableInfo, error)
	Get(context.Context, *PublicDataTableRequest) (*PublicDataTableInfo, error)
	List(context.Context, *PublicDataTableQuery) (*PublicDataTablesInfo, error)
	mustEmbedUnimplementedPublicDataTableServer()
}

// UnimplementedPublicDataTableServer must be embedded to have forward compatible implementations.
type UnimplementedPublicDataTableServer struct {
}

func (UnimplementedPublicDataTableServer) Create(context.Context, *CreatePublicDataTableRequest) (*PublicDataTableInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Create not implemented")
}
func (UnimplementedPublicDataTableServer) Update(context.Context, *UpdatePublicDataTableRequest) (*PublicDataTableInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Update not implemented")
}
func (UnimplementedPublicDataTableServer) Delete(context.Context, *PublicDataTableRequest) (*empty.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Delete not implemented")
}
func (UnimplementedPublicDataTableServer) Load(context.Context, *LoadPublicDataTableRequest) (*PublicDataTableInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Load not implemented")
}
func (UnimplementedPublicDataTableServer) Get(context.Context, *PublicDataTableRequest) (*PublicDataTableInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Get not implemented")
}
func (UnimplementedPublicDataTableServer) List(context.Context, *PublicDataTableQuery) (*PublicDataTablesInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method List not implemented")
}
func (UnimplementedPublicDataTableServer) mustEmbedUnimplementedPublicDataTableServer() {}

// UnsafePublicDataTableServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to PublicDataTableServer will
// result in compilation errors.
type UnsafePublicDataTableServer interface {
	mustEmbedUnimplementedPublicDataTableServer()
}

func RegisterPublicDataTableServer(s grpc.ServiceRegistrar, srv PublicDataTableServer) {
	s.RegisterService(&PublicDataTable_ServiceDesc, srv)
}

func _PublicDataTable_Create_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(CreatePublicDataTableRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(PublicDataTableServer).Create(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: PublicDataTable_Create_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(PublicDataTableServer).Create(ctx, req.(*CreatePublicDataTableRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _PublicDataTable_Update_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(UpdatePublicDataTableRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(PublicDataTableServer).Update(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: PublicDataTable_Update_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(PublicDataTableServer).Update(ctx, req.(*UpdatePublicDataTableRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _PublicDataTable_Delete_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(PublicDataTableRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(PublicDataTableServer).Delete(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: PublicDataTable_Delete_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(PublicDataTableServer).Delete(ctx, req.(*PublicDataTableRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _PublicDataTable_Load_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(LoadPublicDataTableRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(PublicDataTableServer).Load(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: PublicDataTable_Load_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(PublicDataTableServer).Load(ctx, req.(*LoadPublicDataTableRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _PublicDataTable_Get_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(PublicDataTableRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(PublicDataTableServer).Get(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: PublicDataTable_Get_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(PublicDataTableServer).Get(ctx, req.(*PublicDataTableRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _PublicDataTable_List_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(PublicDataTableQuery)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(PublicDataTableServer).List(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: PublicDataTable_List_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(PublicDataTableServer).List(ctx, req.(*PublicDataTableQuery))
	}
	return interceptor(ctx, in, info, handler)
}

// PublicDataTable_ServiceDesc is the grpc.ServiceDesc for PublicDataTable service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var PublicDataTable_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "spaceone.api.data_table.v1.PublicDataTable",
	HandlerType: (*PublicDataTableServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "create",
			Handler:    _PublicDataTable_Create_Handler,
		},
		{
			MethodName: "update",
			Handler:    _PublicDataTable_Update_Handler,
		},
		{
			MethodName: "delete",
			Handler:    _PublicDataTable_Delete_Handler,
		},
		{
			MethodName: "load",
			Handler:    _PublicDataTable_Load_Handler,
		},
		{
			MethodName: "get",
			Handler:    _PublicDataTable_Get_Handler,
		},
		{
			MethodName: "list",
			Handler:    _PublicDataTable_List_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "spaceone/api/dashboard/v1/public_data_table.proto",
}
