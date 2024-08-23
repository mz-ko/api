// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.5.1
// - protoc             v3.6.1
// source: spaceone/api/identity/v2/workspace_group_details.proto

package v2

import (
	context "context"
	empty "github.com/golang/protobuf/ptypes/empty"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.64.0 or later.
const _ = grpc.SupportPackageIsVersion9

const (
	WorkspaceGroupDetails_Update_FullMethodName             = "/spaceone.api.identity.v2.WorkspaceGroupDetails/update"
	WorkspaceGroupDetails_Delete_FullMethodName             = "/spaceone.api.identity.v2.WorkspaceGroupDetails/delete"
	WorkspaceGroupDetails_AddWorkspaces_FullMethodName      = "/spaceone.api.identity.v2.WorkspaceGroupDetails/add_workspaces"
	WorkspaceGroupDetails_RemoveWorkspaces_FullMethodName   = "/spaceone.api.identity.v2.WorkspaceGroupDetails/remove_workspaces"
	WorkspaceGroupDetails_FindUsers_FullMethodName          = "/spaceone.api.identity.v2.WorkspaceGroupDetails/find_users"
	WorkspaceGroupDetails_AddUsers_FullMethodName           = "/spaceone.api.identity.v2.WorkspaceGroupDetails/add_users"
	WorkspaceGroupDetails_RemoveUsers_FullMethodName        = "/spaceone.api.identity.v2.WorkspaceGroupDetails/remove_users"
	WorkspaceGroupDetails_GetWorkspaceGroups_FullMethodName = "/spaceone.api.identity.v2.WorkspaceGroupDetails/get_workspace_groups"
)

// WorkspaceGroupDetailsClient is the client API for WorkspaceGroupDetails service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type WorkspaceGroupDetailsClient interface {
	Update(ctx context.Context, in *UpdateWorkspaceGroupDetailsRequest, opts ...grpc.CallOption) (*WorkspaceGroupDetailsInfo, error)
	Delete(ctx context.Context, in *DeleteWorkspaceGroupDetailsRequest, opts ...grpc.CallOption) (*empty.Empty, error)
	AddWorkspaces(ctx context.Context, in *WorkspacesWorkspaceGroupDetailsRequest, opts ...grpc.CallOption) (*WorkspaceGroupDetailsInfo, error)
	RemoveWorkspaces(ctx context.Context, in *WorkspacesWorkspaceGroupDetailsRequest, opts ...grpc.CallOption) (*WorkspaceGroupDetailsInfo, error)
	FindUsers(ctx context.Context, in *WorkspaceGroupDetailsFindRequest, opts ...grpc.CallOption) (*WorkspaceGroupDetailsUsersSummaryInfo, error)
	AddUsers(ctx context.Context, in *AddUsersWorkspaceGroupDetailsRequest, opts ...grpc.CallOption) (*WorkspaceGroupDetailsInfo, error)
	RemoveUsers(ctx context.Context, in *RemoveUsersWorkspaceGroupDetailsRequest, opts ...grpc.CallOption) (*WorkspaceGroupDetailsInfo, error)
	GetWorkspaceGroups(ctx context.Context, in *WorkspaceGroupDetailsRequest, opts ...grpc.CallOption) (*WorkspaceGroupsDetailsInfo, error)
}

type workspaceGroupDetailsClient struct {
	cc grpc.ClientConnInterface
}

func NewWorkspaceGroupDetailsClient(cc grpc.ClientConnInterface) WorkspaceGroupDetailsClient {
	return &workspaceGroupDetailsClient{cc}
}

func (c *workspaceGroupDetailsClient) Update(ctx context.Context, in *UpdateWorkspaceGroupDetailsRequest, opts ...grpc.CallOption) (*WorkspaceGroupDetailsInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(WorkspaceGroupDetailsInfo)
	err := c.cc.Invoke(ctx, WorkspaceGroupDetails_Update_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *workspaceGroupDetailsClient) Delete(ctx context.Context, in *DeleteWorkspaceGroupDetailsRequest, opts ...grpc.CallOption) (*empty.Empty, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(empty.Empty)
	err := c.cc.Invoke(ctx, WorkspaceGroupDetails_Delete_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *workspaceGroupDetailsClient) AddWorkspaces(ctx context.Context, in *WorkspacesWorkspaceGroupDetailsRequest, opts ...grpc.CallOption) (*WorkspaceGroupDetailsInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(WorkspaceGroupDetailsInfo)
	err := c.cc.Invoke(ctx, WorkspaceGroupDetails_AddWorkspaces_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *workspaceGroupDetailsClient) RemoveWorkspaces(ctx context.Context, in *WorkspacesWorkspaceGroupDetailsRequest, opts ...grpc.CallOption) (*WorkspaceGroupDetailsInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(WorkspaceGroupDetailsInfo)
	err := c.cc.Invoke(ctx, WorkspaceGroupDetails_RemoveWorkspaces_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *workspaceGroupDetailsClient) FindUsers(ctx context.Context, in *WorkspaceGroupDetailsFindRequest, opts ...grpc.CallOption) (*WorkspaceGroupDetailsUsersSummaryInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(WorkspaceGroupDetailsUsersSummaryInfo)
	err := c.cc.Invoke(ctx, WorkspaceGroupDetails_FindUsers_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *workspaceGroupDetailsClient) AddUsers(ctx context.Context, in *AddUsersWorkspaceGroupDetailsRequest, opts ...grpc.CallOption) (*WorkspaceGroupDetailsInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(WorkspaceGroupDetailsInfo)
	err := c.cc.Invoke(ctx, WorkspaceGroupDetails_AddUsers_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *workspaceGroupDetailsClient) RemoveUsers(ctx context.Context, in *RemoveUsersWorkspaceGroupDetailsRequest, opts ...grpc.CallOption) (*WorkspaceGroupDetailsInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(WorkspaceGroupDetailsInfo)
	err := c.cc.Invoke(ctx, WorkspaceGroupDetails_RemoveUsers_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *workspaceGroupDetailsClient) GetWorkspaceGroups(ctx context.Context, in *WorkspaceGroupDetailsRequest, opts ...grpc.CallOption) (*WorkspaceGroupsDetailsInfo, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(WorkspaceGroupsDetailsInfo)
	err := c.cc.Invoke(ctx, WorkspaceGroupDetails_GetWorkspaceGroups_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// WorkspaceGroupDetailsServer is the server API for WorkspaceGroupDetails service.
// All implementations must embed UnimplementedWorkspaceGroupDetailsServer
// for forward compatibility.
type WorkspaceGroupDetailsServer interface {
	Update(context.Context, *UpdateWorkspaceGroupDetailsRequest) (*WorkspaceGroupDetailsInfo, error)
	Delete(context.Context, *DeleteWorkspaceGroupDetailsRequest) (*empty.Empty, error)
	AddWorkspaces(context.Context, *WorkspacesWorkspaceGroupDetailsRequest) (*WorkspaceGroupDetailsInfo, error)
	RemoveWorkspaces(context.Context, *WorkspacesWorkspaceGroupDetailsRequest) (*WorkspaceGroupDetailsInfo, error)
	FindUsers(context.Context, *WorkspaceGroupDetailsFindRequest) (*WorkspaceGroupDetailsUsersSummaryInfo, error)
	AddUsers(context.Context, *AddUsersWorkspaceGroupDetailsRequest) (*WorkspaceGroupDetailsInfo, error)
	RemoveUsers(context.Context, *RemoveUsersWorkspaceGroupDetailsRequest) (*WorkspaceGroupDetailsInfo, error)
	GetWorkspaceGroups(context.Context, *WorkspaceGroupDetailsRequest) (*WorkspaceGroupsDetailsInfo, error)
	mustEmbedUnimplementedWorkspaceGroupDetailsServer()
}

// UnimplementedWorkspaceGroupDetailsServer must be embedded to have
// forward compatible implementations.
//
// NOTE: this should be embedded by value instead of pointer to avoid a nil
// pointer dereference when methods are called.
type UnimplementedWorkspaceGroupDetailsServer struct{}

func (UnimplementedWorkspaceGroupDetailsServer) Update(context.Context, *UpdateWorkspaceGroupDetailsRequest) (*WorkspaceGroupDetailsInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Update not implemented")
}
func (UnimplementedWorkspaceGroupDetailsServer) Delete(context.Context, *DeleteWorkspaceGroupDetailsRequest) (*empty.Empty, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Delete not implemented")
}
func (UnimplementedWorkspaceGroupDetailsServer) AddWorkspaces(context.Context, *WorkspacesWorkspaceGroupDetailsRequest) (*WorkspaceGroupDetailsInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method AddWorkspaces not implemented")
}
func (UnimplementedWorkspaceGroupDetailsServer) RemoveWorkspaces(context.Context, *WorkspacesWorkspaceGroupDetailsRequest) (*WorkspaceGroupDetailsInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method RemoveWorkspaces not implemented")
}
func (UnimplementedWorkspaceGroupDetailsServer) FindUsers(context.Context, *WorkspaceGroupDetailsFindRequest) (*WorkspaceGroupDetailsUsersSummaryInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method FindUsers not implemented")
}
func (UnimplementedWorkspaceGroupDetailsServer) AddUsers(context.Context, *AddUsersWorkspaceGroupDetailsRequest) (*WorkspaceGroupDetailsInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method AddUsers not implemented")
}
func (UnimplementedWorkspaceGroupDetailsServer) RemoveUsers(context.Context, *RemoveUsersWorkspaceGroupDetailsRequest) (*WorkspaceGroupDetailsInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method RemoveUsers not implemented")
}
func (UnimplementedWorkspaceGroupDetailsServer) GetWorkspaceGroups(context.Context, *WorkspaceGroupDetailsRequest) (*WorkspaceGroupsDetailsInfo, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetWorkspaceGroups not implemented")
}
func (UnimplementedWorkspaceGroupDetailsServer) mustEmbedUnimplementedWorkspaceGroupDetailsServer() {}
func (UnimplementedWorkspaceGroupDetailsServer) testEmbeddedByValue()                               {}

// UnsafeWorkspaceGroupDetailsServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to WorkspaceGroupDetailsServer will
// result in compilation errors.
type UnsafeWorkspaceGroupDetailsServer interface {
	mustEmbedUnimplementedWorkspaceGroupDetailsServer()
}

func RegisterWorkspaceGroupDetailsServer(s grpc.ServiceRegistrar, srv WorkspaceGroupDetailsServer) {
	// If the following call pancis, it indicates UnimplementedWorkspaceGroupDetailsServer was
	// embedded by pointer and is nil.  This will cause panics if an
	// unimplemented method is ever invoked, so we test this at initialization
	// time to prevent it from happening at runtime later due to I/O.
	if t, ok := srv.(interface{ testEmbeddedByValue() }); ok {
		t.testEmbeddedByValue()
	}
	s.RegisterService(&WorkspaceGroupDetails_ServiceDesc, srv)
}

func _WorkspaceGroupDetails_Update_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(UpdateWorkspaceGroupDetailsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(WorkspaceGroupDetailsServer).Update(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: WorkspaceGroupDetails_Update_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(WorkspaceGroupDetailsServer).Update(ctx, req.(*UpdateWorkspaceGroupDetailsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _WorkspaceGroupDetails_Delete_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(DeleteWorkspaceGroupDetailsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(WorkspaceGroupDetailsServer).Delete(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: WorkspaceGroupDetails_Delete_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(WorkspaceGroupDetailsServer).Delete(ctx, req.(*DeleteWorkspaceGroupDetailsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _WorkspaceGroupDetails_AddWorkspaces_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(WorkspacesWorkspaceGroupDetailsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(WorkspaceGroupDetailsServer).AddWorkspaces(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: WorkspaceGroupDetails_AddWorkspaces_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(WorkspaceGroupDetailsServer).AddWorkspaces(ctx, req.(*WorkspacesWorkspaceGroupDetailsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _WorkspaceGroupDetails_RemoveWorkspaces_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(WorkspacesWorkspaceGroupDetailsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(WorkspaceGroupDetailsServer).RemoveWorkspaces(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: WorkspaceGroupDetails_RemoveWorkspaces_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(WorkspaceGroupDetailsServer).RemoveWorkspaces(ctx, req.(*WorkspacesWorkspaceGroupDetailsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _WorkspaceGroupDetails_FindUsers_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(WorkspaceGroupDetailsFindRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(WorkspaceGroupDetailsServer).FindUsers(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: WorkspaceGroupDetails_FindUsers_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(WorkspaceGroupDetailsServer).FindUsers(ctx, req.(*WorkspaceGroupDetailsFindRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _WorkspaceGroupDetails_AddUsers_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(AddUsersWorkspaceGroupDetailsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(WorkspaceGroupDetailsServer).AddUsers(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: WorkspaceGroupDetails_AddUsers_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(WorkspaceGroupDetailsServer).AddUsers(ctx, req.(*AddUsersWorkspaceGroupDetailsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _WorkspaceGroupDetails_RemoveUsers_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(RemoveUsersWorkspaceGroupDetailsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(WorkspaceGroupDetailsServer).RemoveUsers(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: WorkspaceGroupDetails_RemoveUsers_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(WorkspaceGroupDetailsServer).RemoveUsers(ctx, req.(*RemoveUsersWorkspaceGroupDetailsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _WorkspaceGroupDetails_GetWorkspaceGroups_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(WorkspaceGroupDetailsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(WorkspaceGroupDetailsServer).GetWorkspaceGroups(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: WorkspaceGroupDetails_GetWorkspaceGroups_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(WorkspaceGroupDetailsServer).GetWorkspaceGroups(ctx, req.(*WorkspaceGroupDetailsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// WorkspaceGroupDetails_ServiceDesc is the grpc.ServiceDesc for WorkspaceGroupDetails service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var WorkspaceGroupDetails_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "spaceone.api.identity.v2.WorkspaceGroupDetails",
	HandlerType: (*WorkspaceGroupDetailsServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "update",
			Handler:    _WorkspaceGroupDetails_Update_Handler,
		},
		{
			MethodName: "delete",
			Handler:    _WorkspaceGroupDetails_Delete_Handler,
		},
		{
			MethodName: "add_workspaces",
			Handler:    _WorkspaceGroupDetails_AddWorkspaces_Handler,
		},
		{
			MethodName: "remove_workspaces",
			Handler:    _WorkspaceGroupDetails_RemoveWorkspaces_Handler,
		},
		{
			MethodName: "find_users",
			Handler:    _WorkspaceGroupDetails_FindUsers_Handler,
		},
		{
			MethodName: "add_users",
			Handler:    _WorkspaceGroupDetails_AddUsers_Handler,
		},
		{
			MethodName: "remove_users",
			Handler:    _WorkspaceGroupDetails_RemoveUsers_Handler,
		},
		{
			MethodName: "get_workspace_groups",
			Handler:    _WorkspaceGroupDetails_GetWorkspaceGroups_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "spaceone/api/identity/v2/workspace_group_details.proto",
}
