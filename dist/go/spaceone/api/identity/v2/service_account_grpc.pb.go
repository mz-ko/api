// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.5.1
// - protoc             v3.6.1
// source: spaceone/api/identity/v2/service_account.proto

package v2

import (
	context "context"
	empty "github.com/golang/protobuf/ptypes/empty"
	_struct "github.com/golang/protobuf/ptypes/struct"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.64.0 or later.
const _ = grpc.SupportPackageIsVersion9

const (
	ServiceAccount_Create_FullMethodName           = "/spaceone.api.identity.v2.ServiceAccount/create"
	ServiceAccount_Update_FullMethodName           = "/spaceone.api.identity.v2.ServiceAccount/update"
	ServiceAccount_UpdateSecretData_FullMethodName = "/spaceone.api.identity.v2.ServiceAccount/update_secret_data"
	ServiceAccount_DeleteSecretData_FullMethodName = "/spaceone.api.identity.v2.ServiceAccount/delete_secret_data"
	ServiceAccount_Delete_FullMethodName           = "/spaceone.api.identity.v2.ServiceAccount/delete"
	ServiceAccount_Get_FullMethodName              = "/spaceone.api.identity.v2.ServiceAccount/get"
	ServiceAccount_List_FullMethodName             = "/spaceone.api.identity.v2.ServiceAccount/list"
	ServiceAccount_Analyze_FullMethodName          = "/spaceone.api.identity.v2.ServiceAccount/analyze"
	ServiceAccount_Stat_FullMethodName             = "/spaceone.api.identity.v2.ServiceAccount/stat"
)

// ServiceAccountClient is the client API for ServiceAccount service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type ServiceAccountClient interface {
	Create(ctx context.Context, in *CreateServiceAccountRequest, opts ...grpc.CallOption) (*ServiceAccountInfo, error)
	Update(ctx context.Context, in *UpdateServiceAccountRequest, opts ...grpc.CallOption) (*ServiceAccountInfo, error)
	UpdateSecretData(ctx context.Context, in *UpdateServiceAccountSecretRequest, opts ...grpc.CallOption) (*ServiceAccountInfo, error)
	DeleteSecretData(ctx context.Context, in *ServiceAccountRequest, opts ...grpc.CallOption) (*ServiceAccountInfo, error)
	Delete(ctx context.Context, in *ServiceAccountRequest, opts ...grpc.CallOption) (*empty.Empty, error)
	Get(ctx context.Context, in *ServiceAccountRequest, opts ...grpc.CallOption) (*ServiceAccountInfo, error)
	List(ctx context.Context, in *ServiceAccountSearchQuery, opts ...grpc.CallOption) (*ServiceAccountsInfo, error)
	Analyze(ctx context.Context, in *ServiceAccountAnalyzeQuery, opts ...grpc.CallOption) (*_struct.Struct, error)
	Stat(ctx context.Context, in *ServiceAccountStatQuery, opts ...grpc.CallOption) (*_struct.Struct, error)
}

type serviceAccountClient struct {
	cc grpc.ClientConnInterface
}

func NewServiceAccountClient(cc grpc.ClientConnInterface) ServiceAccountClient {
	return &serviceAccountClient{cc}
}

func (c *serviceAccountClient) Create(ctx context.Context, in *CreateServiceAccountRequest, opts ...grpc.CallOption) (*ServiceAccountInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(ServiceAccountInfo)
	err := c.cc.Invoke(ctx, ServiceAccount_Create_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *serviceAccountClient) Update(ctx context.Context, in *UpdateServiceAccountRequest, opts ...grpc.CallOption) (*ServiceAccountInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(ServiceAccountInfo)
	err := c.cc.Invoke(ctx, ServiceAccount_Update_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *serviceAccountClient) UpdateSecretData(ctx context.Context, in *UpdateServiceAccountSecretRequest, opts ...grpc.CallOption) (*ServiceAccountInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(ServiceAccountInfo)
	err := c.cc.Invoke(ctx, ServiceAccount_UpdateSecretData_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *serviceAccountClient) DeleteSecretData(ctx context.Context, in *ServiceAccountRequest, opts ...grpc.CallOption) (*ServiceAccountInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(ServiceAccountInfo)
	err := c.cc.Invoke(ctx, ServiceAccount_DeleteSecretData_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *serviceAccountClient) Delete(ctx context.Context, in *ServiceAccountRequest, opts ...grpc.CallOption) (*empty.Empty, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(empty.Empty)
	err := c.cc.Invoke(ctx, ServiceAccount_Delete_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *serviceAccountClient) Get(ctx context.Context, in *ServiceAccountRequest, opts ...grpc.CallOption) (*ServiceAccountInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(ServiceAccountInfo)
	err := c.cc.Invoke(ctx, ServiceAccount_Get_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *serviceAccountClient) List(ctx context.Context, in *ServiceAccountSearchQuery, opts ...grpc.CallOption) (*ServiceAccountsInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(ServiceAccountsInfo)
	err := c.cc.Invoke(ctx, ServiceAccount_List_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *serviceAccountClient) Analyze(ctx context.Context, in *ServiceAccountAnalyzeQuery, opts ...grpc.CallOption) (*_struct.Struct, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(_struct.Struct)
	err := c.cc.Invoke(ctx, ServiceAccount_Analyze_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *serviceAccountClient) Stat(ctx context.Context, in *ServiceAccountStatQuery, opts ...grpc.CallOption) (*_struct.Struct, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(_struct.Struct)
	err := c.cc.Invoke(ctx, ServiceAccount_Stat_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// ServiceAccountServer is the server API for ServiceAccount service.
// All implementations must embed UnimplementedServiceAccountServer
// for forward compatibility.
type ServiceAccountServer interface {
	Create(context.Context, *CreateServiceAccountRequest) (*ServiceAccountInfo, error)
	Update(context.Context, *UpdateServiceAccountRequest) (*ServiceAccountInfo, error)
	UpdateSecretData(context.Context, *UpdateServiceAccountSecretRequest) (*ServiceAccountInfo, error)
	DeleteSecretData(context.Context, *ServiceAccountRequest) (*ServiceAccountInfo, error)
	Delete(context.Context, *ServiceAccountRequest) (*empty.Empty, error)
	Get(context.Context, *ServiceAccountRequest) (*ServiceAccountInfo, error)
	List(context.Context, *ServiceAccountSearchQuery) (*ServiceAccountsInfo, error)
	Analyze(context.Context, *ServiceAccountAnalyzeQuery) (*_struct.Struct, error)
	Stat(context.Context, *ServiceAccountStatQuery) (*_struct.Struct, error)
	mustEmbedUnimplementedServiceAccountServer()
}

// UnimplementedServiceAccountServer must be embedded to have
// forward compatible implementations.
//
// NOTE: this should be embedded by value instead of pointer to avoid a nil
// pointer dereference when methods are called.
type UnimplementedServiceAccountServer struct{}

func (UnimplementedServiceAccountServer) Create(context.Context, *CreateServiceAccountRequest) (*ServiceAccountInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Create not implemented")
}
func (UnimplementedServiceAccountServer) Update(context.Context, *UpdateServiceAccountRequest) (*ServiceAccountInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Update not implemented")
}
func (UnimplementedServiceAccountServer) UpdateSecretData(context.Context, *UpdateServiceAccountSecretRequest) (*ServiceAccountInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method UpdateSecretData not implemented")
}
func (UnimplementedServiceAccountServer) DeleteSecretData(context.Context, *ServiceAccountRequest) (*ServiceAccountInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method DeleteSecretData not implemented")
}
func (UnimplementedServiceAccountServer) Delete(context.Context, *ServiceAccountRequest) (*empty.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Delete not implemented")
}
func (UnimplementedServiceAccountServer) Get(context.Context, *ServiceAccountRequest) (*ServiceAccountInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Get not implemented")
}
func (UnimplementedServiceAccountServer) List(context.Context, *ServiceAccountSearchQuery) (*ServiceAccountsInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method List not implemented")
}
func (UnimplementedServiceAccountServer) Analyze(context.Context, *ServiceAccountAnalyzeQuery) (*_struct.Struct, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Analyze not implemented")
}
func (UnimplementedServiceAccountServer) Stat(context.Context, *ServiceAccountStatQuery) (*_struct.Struct, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Stat not implemented")
}
func (UnimplementedServiceAccountServer) mustEmbedUnimplementedServiceAccountServer() {}
func (UnimplementedServiceAccountServer) testEmbeddedByValue()                        {}

// UnsafeServiceAccountServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to ServiceAccountServer will
// result in compilation errors.
type UnsafeServiceAccountServer interface {
	mustEmbedUnimplementedServiceAccountServer()
}

func RegisterServiceAccountServer(s grpc.ServiceRegistrar, srv ServiceAccountServer) {
	// If the following call pancis, it indicates UnimplementedServiceAccountServer was
	// embedded by pointer and is nil.  This will cause panics if an
	// unimplemented method is ever invoked, so we test this at initialization
	// time to prevent it from happening at runtime later due to I/O.
	if t, ok := srv.(interface{ testEmbeddedByValue() }); ok {
		t.testEmbeddedByValue()
	}
	s.RegisterService(&ServiceAccount_ServiceDesc, srv)
}

func _ServiceAccount_Create_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(CreateServiceAccountRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ServiceAccountServer).Create(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ServiceAccount_Create_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ServiceAccountServer).Create(ctx, req.(*CreateServiceAccountRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ServiceAccount_Update_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(UpdateServiceAccountRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ServiceAccountServer).Update(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ServiceAccount_Update_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ServiceAccountServer).Update(ctx, req.(*UpdateServiceAccountRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ServiceAccount_UpdateSecretData_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(UpdateServiceAccountSecretRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ServiceAccountServer).UpdateSecretData(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ServiceAccount_UpdateSecretData_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ServiceAccountServer).UpdateSecretData(ctx, req.(*UpdateServiceAccountSecretRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ServiceAccount_DeleteSecretData_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ServiceAccountRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ServiceAccountServer).DeleteSecretData(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ServiceAccount_DeleteSecretData_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ServiceAccountServer).DeleteSecretData(ctx, req.(*ServiceAccountRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ServiceAccount_Delete_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ServiceAccountRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ServiceAccountServer).Delete(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ServiceAccount_Delete_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ServiceAccountServer).Delete(ctx, req.(*ServiceAccountRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ServiceAccount_Get_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ServiceAccountRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ServiceAccountServer).Get(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ServiceAccount_Get_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ServiceAccountServer).Get(ctx, req.(*ServiceAccountRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ServiceAccount_List_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ServiceAccountSearchQuery)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ServiceAccountServer).List(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ServiceAccount_List_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ServiceAccountServer).List(ctx, req.(*ServiceAccountSearchQuery))
	}
	return interceptor(ctx, in, info, handler)
}

func _ServiceAccount_Analyze_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ServiceAccountAnalyzeQuery)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ServiceAccountServer).Analyze(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ServiceAccount_Analyze_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ServiceAccountServer).Analyze(ctx, req.(*ServiceAccountAnalyzeQuery))
	}
	return interceptor(ctx, in, info, handler)
}

func _ServiceAccount_Stat_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ServiceAccountStatQuery)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ServiceAccountServer).Stat(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: ServiceAccount_Stat_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ServiceAccountServer).Stat(ctx, req.(*ServiceAccountStatQuery))
	}
	return interceptor(ctx, in, info, handler)
}

// ServiceAccount_ServiceDesc is the grpc.ServiceDesc for ServiceAccount service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var ServiceAccount_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "spaceone.api.identity.v2.ServiceAccount",
	HandlerType: (*ServiceAccountServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "create",
			Handler:    _ServiceAccount_Create_Handler,
		},
		{
			MethodName: "update",
			Handler:    _ServiceAccount_Update_Handler,
		},
		{
			MethodName: "update_secret_data",
			Handler:    _ServiceAccount_UpdateSecretData_Handler,
		},
		{
			MethodName: "delete_secret_data",
			Handler:    _ServiceAccount_DeleteSecretData_Handler,
		},
		{
			MethodName: "delete",
			Handler:    _ServiceAccount_Delete_Handler,
		},
		{
			MethodName: "get",
			Handler:    _ServiceAccount_Get_Handler,
		},
		{
			MethodName: "list",
			Handler:    _ServiceAccount_List_Handler,
		},
		{
			MethodName: "analyze",
			Handler:    _ServiceAccount_Analyze_Handler,
		},
		{
			MethodName: "stat",
			Handler:    _ServiceAccount_Stat_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "spaceone/api/identity/v2/service_account.proto",
}
