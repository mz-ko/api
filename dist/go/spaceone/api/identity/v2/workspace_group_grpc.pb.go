// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.5.1
// - protoc             v3.6.1
// source: spaceone/api/identity/v2/workspace_group.proto

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
	WorkspaceGroup_Create_FullMethodName           = "/spaceone.api.identity.v2.WorkspaceGroup/create"
	WorkspaceGroup_Update_FullMethodName           = "/spaceone.api.identity.v2.WorkspaceGroup/update"
	WorkspaceGroup_Delete_FullMethodName           = "/spaceone.api.identity.v2.WorkspaceGroup/delete"
	WorkspaceGroup_AddWorkspaces_FullMethodName    = "/spaceone.api.identity.v2.WorkspaceGroup/add_workspaces"
	WorkspaceGroup_RemoveWorkspaces_FullMethodName = "/spaceone.api.identity.v2.WorkspaceGroup/remove_workspaces"
	WorkspaceGroup_FindUsers_FullMethodName        = "/spaceone.api.identity.v2.WorkspaceGroup/find_users"
	WorkspaceGroup_AddUsers_FullMethodName         = "/spaceone.api.identity.v2.WorkspaceGroup/add_users"
	WorkspaceGroup_RemoveUsers_FullMethodName      = "/spaceone.api.identity.v2.WorkspaceGroup/remove_users"
	WorkspaceGroup_Get_FullMethodName              = "/spaceone.api.identity.v2.WorkspaceGroup/get"
	WorkspaceGroup_List_FullMethodName             = "/spaceone.api.identity.v2.WorkspaceGroup/list"
	WorkspaceGroup_Stat_FullMethodName             = "/spaceone.api.identity.v2.WorkspaceGroup/stat"
)

// WorkspaceGroupClient is the client API for WorkspaceGroup service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type WorkspaceGroupClient interface {
	Create(ctx context.Context, in *CreateWorkspaceGroupRequest, opts ...grpc.CallOption) (*WorkspaceGroupInfo, error)
	Update(ctx context.Context, in *UpdateWorkspaceGroupRequest, opts ...grpc.CallOption) (*WorkspaceGroupInfo, error)
	Delete(ctx context.Context, in *WorkspaceGroupRequest, opts ...grpc.CallOption) (*empty.Empty, error)
	AddWorkspaces(ctx context.Context, in *WorkspacesWorkspaceGroupRequest, opts ...grpc.CallOption) (*WorkspaceGroupInfo, error)
	RemoveWorkspaces(ctx context.Context, in *WorkspacesWorkspaceGroupRequest, opts ...grpc.CallOption) (*WorkspaceGroupInfo, error)
	FindUsers(ctx context.Context, in *WorkspaceGroupFindRequest, opts ...grpc.CallOption) (*WorkspaceGroupUsersSummaryInfo, error)
	AddUsers(ctx context.Context, in *AddUsersWorkspaceGroupRequest, opts ...grpc.CallOption) (*WorkspaceGroupInfo, error)
	RemoveUsers(ctx context.Context, in *RemoveUsersWorkspaceGroupRequest, opts ...grpc.CallOption) (*WorkspaceGroupInfo, error)
	Get(ctx context.Context, in *WorkspaceGroupRequest, opts ...grpc.CallOption) (*WorkspaceGroupInfo, error)
	List(ctx context.Context, in *WorkspaceGroupSearchQuery, opts ...grpc.CallOption) (*WorkspaceGroupsInfo, error)
	Stat(ctx context.Context, in *WorkspaceGroupStatQuery, opts ...grpc.CallOption) (*_struct.Struct, error)
}

type workspaceGroupClient struct {
	cc grpc.ClientConnInterface
}

func NewWorkspaceGroupClient(cc grpc.ClientConnInterface) WorkspaceGroupClient {
	return &workspaceGroupClient{cc}
}

func (c *workspaceGroupClient) Create(ctx context.Context, in *CreateWorkspaceGroupRequest, opts ...grpc.CallOption) (*WorkspaceGroupInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(WorkspaceGroupInfo)
	err := c.cc.Invoke(ctx, WorkspaceGroup_Create_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *workspaceGroupClient) Update(ctx context.Context, in *UpdateWorkspaceGroupRequest, opts ...grpc.CallOption) (*WorkspaceGroupInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(WorkspaceGroupInfo)
	err := c.cc.Invoke(ctx, WorkspaceGroup_Update_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *workspaceGroupClient) Delete(ctx context.Context, in *WorkspaceGroupRequest, opts ...grpc.CallOption) (*empty.Empty, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(empty.Empty)
	err := c.cc.Invoke(ctx, WorkspaceGroup_Delete_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *workspaceGroupClient) AddWorkspaces(ctx context.Context, in *WorkspacesWorkspaceGroupRequest, opts ...grpc.CallOption) (*WorkspaceGroupInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(WorkspaceGroupInfo)
	err := c.cc.Invoke(ctx, WorkspaceGroup_AddWorkspaces_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *workspaceGroupClient) RemoveWorkspaces(ctx context.Context, in *WorkspacesWorkspaceGroupRequest, opts ...grpc.CallOption) (*WorkspaceGroupInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(WorkspaceGroupInfo)
	err := c.cc.Invoke(ctx, WorkspaceGroup_RemoveWorkspaces_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *workspaceGroupClient) FindUsers(ctx context.Context, in *WorkspaceGroupFindRequest, opts ...grpc.CallOption) (*WorkspaceGroupUsersSummaryInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(WorkspaceGroupUsersSummaryInfo)
	err := c.cc.Invoke(ctx, WorkspaceGroup_FindUsers_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *workspaceGroupClient) AddUsers(ctx context.Context, in *AddUsersWorkspaceGroupRequest, opts ...grpc.CallOption) (*WorkspaceGroupInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(WorkspaceGroupInfo)
	err := c.cc.Invoke(ctx, WorkspaceGroup_AddUsers_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *workspaceGroupClient) RemoveUsers(ctx context.Context, in *RemoveUsersWorkspaceGroupRequest, opts ...grpc.CallOption) (*WorkspaceGroupInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(WorkspaceGroupInfo)
	err := c.cc.Invoke(ctx, WorkspaceGroup_RemoveUsers_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *workspaceGroupClient) Get(ctx context.Context, in *WorkspaceGroupRequest, opts ...grpc.CallOption) (*WorkspaceGroupInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(WorkspaceGroupInfo)
	err := c.cc.Invoke(ctx, WorkspaceGroup_Get_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *workspaceGroupClient) List(ctx context.Context, in *WorkspaceGroupSearchQuery, opts ...grpc.CallOption) (*WorkspaceGroupsInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(WorkspaceGroupsInfo)
	err := c.cc.Invoke(ctx, WorkspaceGroup_List_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *workspaceGroupClient) Stat(ctx context.Context, in *WorkspaceGroupStatQuery, opts ...grpc.CallOption) (*_struct.Struct, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(_struct.Struct)
	err := c.cc.Invoke(ctx, WorkspaceGroup_Stat_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// WorkspaceGroupServer is the server API for WorkspaceGroup service.
// All implementations must embed UnimplementedWorkspaceGroupServer
// for forward compatibility.
type WorkspaceGroupServer interface {
	Create(context.Context, *CreateWorkspaceGroupRequest) (*WorkspaceGroupInfo, error)
	Update(context.Context, *UpdateWorkspaceGroupRequest) (*WorkspaceGroupInfo, error)
	Delete(context.Context, *WorkspaceGroupRequest) (*empty.Empty, error)
	AddWorkspaces(context.Context, *WorkspacesWorkspaceGroupRequest) (*WorkspaceGroupInfo, error)
	RemoveWorkspaces(context.Context, *WorkspacesWorkspaceGroupRequest) (*WorkspaceGroupInfo, error)
	FindUsers(context.Context, *WorkspaceGroupFindRequest) (*WorkspaceGroupUsersSummaryInfo, error)
	AddUsers(context.Context, *AddUsersWorkspaceGroupRequest) (*WorkspaceGroupInfo, error)
	RemoveUsers(context.Context, *RemoveUsersWorkspaceGroupRequest) (*WorkspaceGroupInfo, error)
	Get(context.Context, *WorkspaceGroupRequest) (*WorkspaceGroupInfo, error)
	List(context.Context, *WorkspaceGroupSearchQuery) (*WorkspaceGroupsInfo, error)
	Stat(context.Context, *WorkspaceGroupStatQuery) (*_struct.Struct, error)
	mustEmbedUnimplementedWorkspaceGroupServer()
}

// UnimplementedWorkspaceGroupServer must be embedded to have
// forward compatible implementations.
//
// NOTE: this should be embedded by value instead of pointer to avoid a nil
// pointer dereference when methods are called.
type UnimplementedWorkspaceGroupServer struct{}

func (UnimplementedWorkspaceGroupServer) Create(context.Context, *CreateWorkspaceGroupRequest) (*WorkspaceGroupInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Create not implemented")
}
func (UnimplementedWorkspaceGroupServer) Update(context.Context, *UpdateWorkspaceGroupRequest) (*WorkspaceGroupInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Update not implemented")
}
func (UnimplementedWorkspaceGroupServer) Delete(context.Context, *WorkspaceGroupRequest) (*empty.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Delete not implemented")
}
func (UnimplementedWorkspaceGroupServer) AddWorkspaces(context.Context, *WorkspacesWorkspaceGroupRequest) (*WorkspaceGroupInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method AddWorkspaces not implemented")
}
func (UnimplementedWorkspaceGroupServer) RemoveWorkspaces(context.Context, *WorkspacesWorkspaceGroupRequest) (*WorkspaceGroupInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method RemoveWorkspaces not implemented")
}
func (UnimplementedWorkspaceGroupServer) FindUsers(context.Context, *WorkspaceGroupFindRequest) (*WorkspaceGroupUsersSummaryInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method FindUsers not implemented")
}
func (UnimplementedWorkspaceGroupServer) AddUsers(context.Context, *AddUsersWorkspaceGroupRequest) (*WorkspaceGroupInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method AddUsers not implemented")
}
func (UnimplementedWorkspaceGroupServer) RemoveUsers(context.Context, *RemoveUsersWorkspaceGroupRequest) (*WorkspaceGroupInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method RemoveUsers not implemented")
}
func (UnimplementedWorkspaceGroupServer) Get(context.Context, *WorkspaceGroupRequest) (*WorkspaceGroupInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Get not implemented")
}
func (UnimplementedWorkspaceGroupServer) List(context.Context, *WorkspaceGroupSearchQuery) (*WorkspaceGroupsInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method List not implemented")
}
func (UnimplementedWorkspaceGroupServer) Stat(context.Context, *WorkspaceGroupStatQuery) (*_struct.Struct, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Stat not implemented")
}
func (UnimplementedWorkspaceGroupServer) mustEmbedUnimplementedWorkspaceGroupServer() {}
func (UnimplementedWorkspaceGroupServer) testEmbeddedByValue()                        {}

// UnsafeWorkspaceGroupServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to WorkspaceGroupServer will
// result in compilation errors.
type UnsafeWorkspaceGroupServer interface {
	mustEmbedUnimplementedWorkspaceGroupServer()
}

func RegisterWorkspaceGroupServer(s grpc.ServiceRegistrar, srv WorkspaceGroupServer) {
	// If the following call pancis, it indicates UnimplementedWorkspaceGroupServer was
	// embedded by pointer and is nil.  This will cause panics if an
	// unimplemented method is ever invoked, so we test this at initialization
	// time to prevent it from happening at runtime later due to I/O.
	if t, ok := srv.(interface{ testEmbeddedByValue() }); ok {
		t.testEmbeddedByValue()
	}
	s.RegisterService(&WorkspaceGroup_ServiceDesc, srv)
}

func _WorkspaceGroup_Create_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(CreateWorkspaceGroupRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(WorkspaceGroupServer).Create(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: WorkspaceGroup_Create_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(WorkspaceGroupServer).Create(ctx, req.(*CreateWorkspaceGroupRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _WorkspaceGroup_Update_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(UpdateWorkspaceGroupRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(WorkspaceGroupServer).Update(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: WorkspaceGroup_Update_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(WorkspaceGroupServer).Update(ctx, req.(*UpdateWorkspaceGroupRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _WorkspaceGroup_Delete_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(WorkspaceGroupRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(WorkspaceGroupServer).Delete(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: WorkspaceGroup_Delete_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(WorkspaceGroupServer).Delete(ctx, req.(*WorkspaceGroupRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _WorkspaceGroup_AddWorkspaces_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(WorkspacesWorkspaceGroupRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(WorkspaceGroupServer).AddWorkspaces(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: WorkspaceGroup_AddWorkspaces_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(WorkspaceGroupServer).AddWorkspaces(ctx, req.(*WorkspacesWorkspaceGroupRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _WorkspaceGroup_RemoveWorkspaces_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(WorkspacesWorkspaceGroupRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(WorkspaceGroupServer).RemoveWorkspaces(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: WorkspaceGroup_RemoveWorkspaces_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(WorkspaceGroupServer).RemoveWorkspaces(ctx, req.(*WorkspacesWorkspaceGroupRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _WorkspaceGroup_FindUsers_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(WorkspaceGroupFindRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(WorkspaceGroupServer).FindUsers(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: WorkspaceGroup_FindUsers_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(WorkspaceGroupServer).FindUsers(ctx, req.(*WorkspaceGroupFindRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _WorkspaceGroup_AddUsers_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(AddUsersWorkspaceGroupRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(WorkspaceGroupServer).AddUsers(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: WorkspaceGroup_AddUsers_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(WorkspaceGroupServer).AddUsers(ctx, req.(*AddUsersWorkspaceGroupRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _WorkspaceGroup_RemoveUsers_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(RemoveUsersWorkspaceGroupRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(WorkspaceGroupServer).RemoveUsers(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: WorkspaceGroup_RemoveUsers_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(WorkspaceGroupServer).RemoveUsers(ctx, req.(*RemoveUsersWorkspaceGroupRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _WorkspaceGroup_Get_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(WorkspaceGroupRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(WorkspaceGroupServer).Get(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: WorkspaceGroup_Get_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(WorkspaceGroupServer).Get(ctx, req.(*WorkspaceGroupRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _WorkspaceGroup_List_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(WorkspaceGroupSearchQuery)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(WorkspaceGroupServer).List(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: WorkspaceGroup_List_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(WorkspaceGroupServer).List(ctx, req.(*WorkspaceGroupSearchQuery))
	}
	return interceptor(ctx, in, info, handler)
}

func _WorkspaceGroup_Stat_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(WorkspaceGroupStatQuery)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(WorkspaceGroupServer).Stat(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: WorkspaceGroup_Stat_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(WorkspaceGroupServer).Stat(ctx, req.(*WorkspaceGroupStatQuery))
	}
	return interceptor(ctx, in, info, handler)
}

// WorkspaceGroup_ServiceDesc is the grpc.ServiceDesc for WorkspaceGroup service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var WorkspaceGroup_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "spaceone.api.identity.v2.WorkspaceGroup",
	HandlerType: (*WorkspaceGroupServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "create",
			Handler:    _WorkspaceGroup_Create_Handler,
		},
		{
			MethodName: "update",
			Handler:    _WorkspaceGroup_Update_Handler,
		},
		{
			MethodName: "delete",
			Handler:    _WorkspaceGroup_Delete_Handler,
		},
		{
			MethodName: "add_workspaces",
			Handler:    _WorkspaceGroup_AddWorkspaces_Handler,
		},
		{
			MethodName: "remove_workspaces",
			Handler:    _WorkspaceGroup_RemoveWorkspaces_Handler,
		},
		{
			MethodName: "find_users",
			Handler:    _WorkspaceGroup_FindUsers_Handler,
		},
		{
			MethodName: "add_users",
			Handler:    _WorkspaceGroup_AddUsers_Handler,
		},
		{
			MethodName: "remove_users",
			Handler:    _WorkspaceGroup_RemoveUsers_Handler,
		},
		{
			MethodName: "get",
			Handler:    _WorkspaceGroup_Get_Handler,
		},
		{
			MethodName: "list",
			Handler:    _WorkspaceGroup_List_Handler,
		},
		{
			MethodName: "stat",
			Handler:    _WorkspaceGroup_Stat_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "spaceone/api/identity/v2/workspace_group.proto",
}
