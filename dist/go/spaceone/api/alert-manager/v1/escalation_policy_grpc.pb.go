// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.5.1
// - protoc             v3.6.1
// source: spaceone/api/alert_manager/v1/escalation_policy.proto

package v1

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
	EscalationPolicy_Create_FullMethodName = "/spaceone.api.alert_manager.v1.EscalationPolicy/create"
	EscalationPolicy_Update_FullMethodName = "/spaceone.api.alert_manager.v1.EscalationPolicy/update"
	EscalationPolicy_Delete_FullMethodName = "/spaceone.api.alert_manager.v1.EscalationPolicy/delete"
	EscalationPolicy_Get_FullMethodName    = "/spaceone.api.alert_manager.v1.EscalationPolicy/get"
	EscalationPolicy_List_FullMethodName   = "/spaceone.api.alert_manager.v1.EscalationPolicy/list"
	EscalationPolicy_Stat_FullMethodName   = "/spaceone.api.alert_manager.v1.EscalationPolicy/stat"
)

// EscalationPolicyClient is the client API for EscalationPolicy service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type EscalationPolicyClient interface {
	Create(ctx context.Context, in *EscalationPolicyCreateRequest, opts ...grpc.CallOption) (*EscalationPolicyInfo, error)
	Update(ctx context.Context, in *EscalationPolicyUpdateRequest, opts ...grpc.CallOption) (*EscalationPolicyInfo, error)
	Delete(ctx context.Context, in *EscalationPolicyRequest, opts ...grpc.CallOption) (*empty.Empty, error)
	Get(ctx context.Context, in *EscalationPolicyRequest, opts ...grpc.CallOption) (*EscalationPolicyInfo, error)
	List(ctx context.Context, in *EscalationPolicySearchQuery, opts ...grpc.CallOption) (*EscalationPoliciesInfo, error)
	Stat(ctx context.Context, in *EscalationPolicyStatQuery, opts ...grpc.CallOption) (*_struct.Struct, error)
}

type escalationPolicyClient struct {
	cc grpc.ClientConnInterface
}

func NewEscalationPolicyClient(cc grpc.ClientConnInterface) EscalationPolicyClient {
	return &escalationPolicyClient{cc}
}

func (c *escalationPolicyClient) Create(ctx context.Context, in *EscalationPolicyCreateRequest, opts ...grpc.CallOption) (*EscalationPolicyInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(EscalationPolicyInfo)
	err := c.cc.Invoke(ctx, EscalationPolicy_Create_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *escalationPolicyClient) Update(ctx context.Context, in *EscalationPolicyUpdateRequest, opts ...grpc.CallOption) (*EscalationPolicyInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(EscalationPolicyInfo)
	err := c.cc.Invoke(ctx, EscalationPolicy_Update_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *escalationPolicyClient) Delete(ctx context.Context, in *EscalationPolicyRequest, opts ...grpc.CallOption) (*empty.Empty, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(empty.Empty)
	err := c.cc.Invoke(ctx, EscalationPolicy_Delete_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *escalationPolicyClient) Get(ctx context.Context, in *EscalationPolicyRequest, opts ...grpc.CallOption) (*EscalationPolicyInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(EscalationPolicyInfo)
	err := c.cc.Invoke(ctx, EscalationPolicy_Get_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *escalationPolicyClient) List(ctx context.Context, in *EscalationPolicySearchQuery, opts ...grpc.CallOption) (*EscalationPoliciesInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(EscalationPoliciesInfo)
	err := c.cc.Invoke(ctx, EscalationPolicy_List_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *escalationPolicyClient) Stat(ctx context.Context, in *EscalationPolicyStatQuery, opts ...grpc.CallOption) (*_struct.Struct, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(_struct.Struct)
	err := c.cc.Invoke(ctx, EscalationPolicy_Stat_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// EscalationPolicyServer is the server API for EscalationPolicy service.
// All implementations must embed UnimplementedEscalationPolicyServer
// for forward compatibility.
type EscalationPolicyServer interface {
	Create(context.Context, *EscalationPolicyCreateRequest) (*EscalationPolicyInfo, error)
	Update(context.Context, *EscalationPolicyUpdateRequest) (*EscalationPolicyInfo, error)
	Delete(context.Context, *EscalationPolicyRequest) (*empty.Empty, error)
	Get(context.Context, *EscalationPolicyRequest) (*EscalationPolicyInfo, error)
	List(context.Context, *EscalationPolicySearchQuery) (*EscalationPoliciesInfo, error)
	Stat(context.Context, *EscalationPolicyStatQuery) (*_struct.Struct, error)
	mustEmbedUnimplementedEscalationPolicyServer()
}

// UnimplementedEscalationPolicyServer must be embedded to have
// forward compatible implementations.
//
// NOTE: this should be embedded by value instead of pointer to avoid a nil
// pointer dereference when methods are called.
type UnimplementedEscalationPolicyServer struct{}

func (UnimplementedEscalationPolicyServer) Create(context.Context, *EscalationPolicyCreateRequest) (*EscalationPolicyInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Create not implemented")
}
func (UnimplementedEscalationPolicyServer) Update(context.Context, *EscalationPolicyUpdateRequest) (*EscalationPolicyInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Update not implemented")
}
func (UnimplementedEscalationPolicyServer) Delete(context.Context, *EscalationPolicyRequest) (*empty.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Delete not implemented")
}
func (UnimplementedEscalationPolicyServer) Get(context.Context, *EscalationPolicyRequest) (*EscalationPolicyInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Get not implemented")
}
func (UnimplementedEscalationPolicyServer) List(context.Context, *EscalationPolicySearchQuery) (*EscalationPoliciesInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method List not implemented")
}
func (UnimplementedEscalationPolicyServer) Stat(context.Context, *EscalationPolicyStatQuery) (*_struct.Struct, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Stat not implemented")
}
func (UnimplementedEscalationPolicyServer) mustEmbedUnimplementedEscalationPolicyServer() {}
func (UnimplementedEscalationPolicyServer) testEmbeddedByValue()                          {}

// UnsafeEscalationPolicyServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to EscalationPolicyServer will
// result in compilation errors.
type UnsafeEscalationPolicyServer interface {
	mustEmbedUnimplementedEscalationPolicyServer()
}

func RegisterEscalationPolicyServer(s grpc.ServiceRegistrar, srv EscalationPolicyServer) {
	// If the following call pancis, it indicates UnimplementedEscalationPolicyServer was
	// embedded by pointer and is nil.  This will cause panics if an
	// unimplemented method is ever invoked, so we test this at initialization
	// time to prevent it from happening at runtime later due to I/O.
	if t, ok := srv.(interface{ testEmbeddedByValue() }); ok {
		t.testEmbeddedByValue()
	}
	s.RegisterService(&EscalationPolicy_ServiceDesc, srv)
}

func _EscalationPolicy_Create_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(EscalationPolicyCreateRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EscalationPolicyServer).Create(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: EscalationPolicy_Create_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EscalationPolicyServer).Create(ctx, req.(*EscalationPolicyCreateRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _EscalationPolicy_Update_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(EscalationPolicyUpdateRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EscalationPolicyServer).Update(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: EscalationPolicy_Update_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EscalationPolicyServer).Update(ctx, req.(*EscalationPolicyUpdateRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _EscalationPolicy_Delete_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(EscalationPolicyRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EscalationPolicyServer).Delete(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: EscalationPolicy_Delete_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EscalationPolicyServer).Delete(ctx, req.(*EscalationPolicyRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _EscalationPolicy_Get_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(EscalationPolicyRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EscalationPolicyServer).Get(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: EscalationPolicy_Get_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EscalationPolicyServer).Get(ctx, req.(*EscalationPolicyRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _EscalationPolicy_List_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(EscalationPolicySearchQuery)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EscalationPolicyServer).List(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: EscalationPolicy_List_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EscalationPolicyServer).List(ctx, req.(*EscalationPolicySearchQuery))
	}
	return interceptor(ctx, in, info, handler)
}

func _EscalationPolicy_Stat_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(EscalationPolicyStatQuery)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EscalationPolicyServer).Stat(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: EscalationPolicy_Stat_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EscalationPolicyServer).Stat(ctx, req.(*EscalationPolicyStatQuery))
	}
	return interceptor(ctx, in, info, handler)
}

// EscalationPolicy_ServiceDesc is the grpc.ServiceDesc for EscalationPolicy service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var EscalationPolicy_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "spaceone.api.alert_manager.v1.EscalationPolicy",
	HandlerType: (*EscalationPolicyServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "create",
			Handler:    _EscalationPolicy_Create_Handler,
		},
		{
			MethodName: "update",
			Handler:    _EscalationPolicy_Update_Handler,
		},
		{
			MethodName: "delete",
			Handler:    _EscalationPolicy_Delete_Handler,
		},
		{
			MethodName: "get",
			Handler:    _EscalationPolicy_Get_Handler,
		},
		{
			MethodName: "list",
			Handler:    _EscalationPolicy_List_Handler,
		},
		{
			MethodName: "stat",
			Handler:    _EscalationPolicy_Stat_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "spaceone/api/alert_manager/v1/escalation_policy.proto",
}