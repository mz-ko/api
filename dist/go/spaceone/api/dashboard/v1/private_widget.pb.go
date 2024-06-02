// description of widget

// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.34.1
// 	protoc        v3.6.1
// source: spaceone/api/dashboard/v1/private_widget.proto

package v1

import (
	v2 "github.com/cloudforet-io/api/dist/go/spaceone/api/core/v2"
	empty "github.com/golang/protobuf/ptypes/empty"
	_struct "github.com/golang/protobuf/ptypes/struct"
	_ "google.golang.org/genproto/googleapis/api/annotations"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type CreatePrivateWidgetRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	DashboardId string `protobuf:"bytes,1,opt,name=dashboard_id,json=dashboardId,proto3" json:"dashboard_id,omitempty"`
	// +optional
	Name string `protobuf:"bytes,2,opt,name=name,proto3" json:"name,omitempty"`
	// +optional
	Description string `protobuf:"bytes,3,opt,name=description,proto3" json:"description,omitempty"`
	// +optional
	WidgetType string `protobuf:"bytes,4,opt,name=widget_type,json=widgetType,proto3" json:"widget_type,omitempty"`
	// +optional
	Options *_struct.Struct `protobuf:"bytes,5,opt,name=options,proto3" json:"options,omitempty"`
	// +optional
	Tags *_struct.Struct `protobuf:"bytes,6,opt,name=tags,proto3" json:"tags,omitempty"`
}

func (x *CreatePrivateWidgetRequest) Reset() {
	*x = CreatePrivateWidgetRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_spaceone_api_dashboard_v1_private_widget_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *CreatePrivateWidgetRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*CreatePrivateWidgetRequest) ProtoMessage() {}

func (x *CreatePrivateWidgetRequest) ProtoReflect() protoreflect.Message {
	mi := &file_spaceone_api_dashboard_v1_private_widget_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use CreatePrivateWidgetRequest.ProtoReflect.Descriptor instead.
func (*CreatePrivateWidgetRequest) Descriptor() ([]byte, []int) {
	return file_spaceone_api_dashboard_v1_private_widget_proto_rawDescGZIP(), []int{0}
}

func (x *CreatePrivateWidgetRequest) GetDashboardId() string {
	if x != nil {
		return x.DashboardId
	}
	return ""
}

func (x *CreatePrivateWidgetRequest) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *CreatePrivateWidgetRequest) GetDescription() string {
	if x != nil {
		return x.Description
	}
	return ""
}

func (x *CreatePrivateWidgetRequest) GetWidgetType() string {
	if x != nil {
		return x.WidgetType
	}
	return ""
}

func (x *CreatePrivateWidgetRequest) GetOptions() *_struct.Struct {
	if x != nil {
		return x.Options
	}
	return nil
}

func (x *CreatePrivateWidgetRequest) GetTags() *_struct.Struct {
	if x != nil {
		return x.Tags
	}
	return nil
}

type UpdatePrivateWidgetRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	WidgetId string `protobuf:"bytes,1,opt,name=widget_id,json=widgetId,proto3" json:"widget_id,omitempty"`
	// +optional
	Name string `protobuf:"bytes,2,opt,name=name,proto3" json:"name,omitempty"`
	// +optional
	Description string `protobuf:"bytes,3,opt,name=description,proto3" json:"description,omitempty"`
	// +optional
	WidgetType string `protobuf:"bytes,4,opt,name=widget_type,json=widgetType,proto3" json:"widget_type,omitempty"`
	// +optional
	Options *_struct.Struct `protobuf:"bytes,5,opt,name=options,proto3" json:"options,omitempty"`
	// +optional
	Tags *_struct.Struct `protobuf:"bytes,6,opt,name=tags,proto3" json:"tags,omitempty"`
}

func (x *UpdatePrivateWidgetRequest) Reset() {
	*x = UpdatePrivateWidgetRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_spaceone_api_dashboard_v1_private_widget_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *UpdatePrivateWidgetRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*UpdatePrivateWidgetRequest) ProtoMessage() {}

func (x *UpdatePrivateWidgetRequest) ProtoReflect() protoreflect.Message {
	mi := &file_spaceone_api_dashboard_v1_private_widget_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use UpdatePrivateWidgetRequest.ProtoReflect.Descriptor instead.
func (*UpdatePrivateWidgetRequest) Descriptor() ([]byte, []int) {
	return file_spaceone_api_dashboard_v1_private_widget_proto_rawDescGZIP(), []int{1}
}

func (x *UpdatePrivateWidgetRequest) GetWidgetId() string {
	if x != nil {
		return x.WidgetId
	}
	return ""
}

func (x *UpdatePrivateWidgetRequest) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *UpdatePrivateWidgetRequest) GetDescription() string {
	if x != nil {
		return x.Description
	}
	return ""
}

func (x *UpdatePrivateWidgetRequest) GetWidgetType() string {
	if x != nil {
		return x.WidgetType
	}
	return ""
}

func (x *UpdatePrivateWidgetRequest) GetOptions() *_struct.Struct {
	if x != nil {
		return x.Options
	}
	return nil
}

func (x *UpdatePrivateWidgetRequest) GetTags() *_struct.Struct {
	if x != nil {
		return x.Tags
	}
	return nil
}

type PrivateWidgetRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	WidgetId string `protobuf:"bytes,1,opt,name=widget_id,json=widgetId,proto3" json:"widget_id,omitempty"`
}

func (x *PrivateWidgetRequest) Reset() {
	*x = PrivateWidgetRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_spaceone_api_dashboard_v1_private_widget_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *PrivateWidgetRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*PrivateWidgetRequest) ProtoMessage() {}

func (x *PrivateWidgetRequest) ProtoReflect() protoreflect.Message {
	mi := &file_spaceone_api_dashboard_v1_private_widget_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use PrivateWidgetRequest.ProtoReflect.Descriptor instead.
func (*PrivateWidgetRequest) Descriptor() ([]byte, []int) {
	return file_spaceone_api_dashboard_v1_private_widget_proto_rawDescGZIP(), []int{2}
}

func (x *PrivateWidgetRequest) GetWidgetId() string {
	if x != nil {
		return x.WidgetId
	}
	return ""
}

type LoadPrivateWidgetRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	WidgetId string                     `protobuf:"bytes,1,opt,name=widget_id,json=widgetId,proto3" json:"widget_id,omitempty"`
	Query    *v2.TimeSeriesAnalyzeQuery `protobuf:"bytes,2,opt,name=query,proto3" json:"query,omitempty"`
	// +optional
	Vars *_struct.Struct `protobuf:"bytes,3,opt,name=vars,proto3" json:"vars,omitempty"`
}

func (x *LoadPrivateWidgetRequest) Reset() {
	*x = LoadPrivateWidgetRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_spaceone_api_dashboard_v1_private_widget_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *LoadPrivateWidgetRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*LoadPrivateWidgetRequest) ProtoMessage() {}

func (x *LoadPrivateWidgetRequest) ProtoReflect() protoreflect.Message {
	mi := &file_spaceone_api_dashboard_v1_private_widget_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use LoadPrivateWidgetRequest.ProtoReflect.Descriptor instead.
func (*LoadPrivateWidgetRequest) Descriptor() ([]byte, []int) {
	return file_spaceone_api_dashboard_v1_private_widget_proto_rawDescGZIP(), []int{3}
}

func (x *LoadPrivateWidgetRequest) GetWidgetId() string {
	if x != nil {
		return x.WidgetId
	}
	return ""
}

func (x *LoadPrivateWidgetRequest) GetQuery() *v2.TimeSeriesAnalyzeQuery {
	if x != nil {
		return x.Query
	}
	return nil
}

func (x *LoadPrivateWidgetRequest) GetVars() *_struct.Struct {
	if x != nil {
		return x.Vars
	}
	return nil
}

type PrivateWidgetQuery struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// +optional
	Query       *v2.Query `protobuf:"bytes,1,opt,name=query,proto3" json:"query,omitempty"`
	DashboardId string    `protobuf:"bytes,2,opt,name=dashboard_id,json=dashboardId,proto3" json:"dashboard_id,omitempty"`
	// +optional
	WidgetId string `protobuf:"bytes,3,opt,name=widget_id,json=widgetId,proto3" json:"widget_id,omitempty"`
	// +optional
	Name string `protobuf:"bytes,4,opt,name=name,proto3" json:"name,omitempty"`
}

func (x *PrivateWidgetQuery) Reset() {
	*x = PrivateWidgetQuery{}
	if protoimpl.UnsafeEnabled {
		mi := &file_spaceone_api_dashboard_v1_private_widget_proto_msgTypes[4]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *PrivateWidgetQuery) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*PrivateWidgetQuery) ProtoMessage() {}

func (x *PrivateWidgetQuery) ProtoReflect() protoreflect.Message {
	mi := &file_spaceone_api_dashboard_v1_private_widget_proto_msgTypes[4]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use PrivateWidgetQuery.ProtoReflect.Descriptor instead.
func (*PrivateWidgetQuery) Descriptor() ([]byte, []int) {
	return file_spaceone_api_dashboard_v1_private_widget_proto_rawDescGZIP(), []int{4}
}

func (x *PrivateWidgetQuery) GetQuery() *v2.Query {
	if x != nil {
		return x.Query
	}
	return nil
}

func (x *PrivateWidgetQuery) GetDashboardId() string {
	if x != nil {
		return x.DashboardId
	}
	return ""
}

func (x *PrivateWidgetQuery) GetWidgetId() string {
	if x != nil {
		return x.WidgetId
	}
	return ""
}

func (x *PrivateWidgetQuery) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

type PrivateWidgetInfo struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	WidgetId    string          `protobuf:"bytes,1,opt,name=widget_id,json=widgetId,proto3" json:"widget_id,omitempty"`
	Name        string          `protobuf:"bytes,2,opt,name=name,proto3" json:"name,omitempty"`
	Description string          `protobuf:"bytes,3,opt,name=description,proto3" json:"description,omitempty"`
	WidgetType  string          `protobuf:"bytes,4,opt,name=widget_type,json=widgetType,proto3" json:"widget_type,omitempty"`
	Options     *_struct.Struct `protobuf:"bytes,5,opt,name=options,proto3" json:"options,omitempty"`
	Tags        *_struct.Struct `protobuf:"bytes,6,opt,name=tags,proto3" json:"tags,omitempty"`
	DomainId    string          `protobuf:"bytes,21,opt,name=domain_id,json=domainId,proto3" json:"domain_id,omitempty"`
	UserId      string          `protobuf:"bytes,22,opt,name=user_id,json=userId,proto3" json:"user_id,omitempty"`
	DashboardId string          `protobuf:"bytes,23,opt,name=dashboard_id,json=dashboardId,proto3" json:"dashboard_id,omitempty"`
	CreatedAt   string          `protobuf:"bytes,31,opt,name=created_at,json=createdAt,proto3" json:"created_at,omitempty"`
	UpdatedAt   string          `protobuf:"bytes,32,opt,name=updated_at,json=updatedAt,proto3" json:"updated_at,omitempty"`
}

func (x *PrivateWidgetInfo) Reset() {
	*x = PrivateWidgetInfo{}
	if protoimpl.UnsafeEnabled {
		mi := &file_spaceone_api_dashboard_v1_private_widget_proto_msgTypes[5]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *PrivateWidgetInfo) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*PrivateWidgetInfo) ProtoMessage() {}

func (x *PrivateWidgetInfo) ProtoReflect() protoreflect.Message {
	mi := &file_spaceone_api_dashboard_v1_private_widget_proto_msgTypes[5]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use PrivateWidgetInfo.ProtoReflect.Descriptor instead.
func (*PrivateWidgetInfo) Descriptor() ([]byte, []int) {
	return file_spaceone_api_dashboard_v1_private_widget_proto_rawDescGZIP(), []int{5}
}

func (x *PrivateWidgetInfo) GetWidgetId() string {
	if x != nil {
		return x.WidgetId
	}
	return ""
}

func (x *PrivateWidgetInfo) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *PrivateWidgetInfo) GetDescription() string {
	if x != nil {
		return x.Description
	}
	return ""
}

func (x *PrivateWidgetInfo) GetWidgetType() string {
	if x != nil {
		return x.WidgetType
	}
	return ""
}

func (x *PrivateWidgetInfo) GetOptions() *_struct.Struct {
	if x != nil {
		return x.Options
	}
	return nil
}

func (x *PrivateWidgetInfo) GetTags() *_struct.Struct {
	if x != nil {
		return x.Tags
	}
	return nil
}

func (x *PrivateWidgetInfo) GetDomainId() string {
	if x != nil {
		return x.DomainId
	}
	return ""
}

func (x *PrivateWidgetInfo) GetUserId() string {
	if x != nil {
		return x.UserId
	}
	return ""
}

func (x *PrivateWidgetInfo) GetDashboardId() string {
	if x != nil {
		return x.DashboardId
	}
	return ""
}

func (x *PrivateWidgetInfo) GetCreatedAt() string {
	if x != nil {
		return x.CreatedAt
	}
	return ""
}

func (x *PrivateWidgetInfo) GetUpdatedAt() string {
	if x != nil {
		return x.UpdatedAt
	}
	return ""
}

type PrivateWidgetsInfo struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Results    []*PrivateWidgetInfo `protobuf:"bytes,1,rep,name=results,proto3" json:"results,omitempty"`
	TotalCount int32                `protobuf:"varint,2,opt,name=total_count,json=totalCount,proto3" json:"total_count,omitempty"`
}

func (x *PrivateWidgetsInfo) Reset() {
	*x = PrivateWidgetsInfo{}
	if protoimpl.UnsafeEnabled {
		mi := &file_spaceone_api_dashboard_v1_private_widget_proto_msgTypes[6]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *PrivateWidgetsInfo) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*PrivateWidgetsInfo) ProtoMessage() {}

func (x *PrivateWidgetsInfo) ProtoReflect() protoreflect.Message {
	mi := &file_spaceone_api_dashboard_v1_private_widget_proto_msgTypes[6]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use PrivateWidgetsInfo.ProtoReflect.Descriptor instead.
func (*PrivateWidgetsInfo) Descriptor() ([]byte, []int) {
	return file_spaceone_api_dashboard_v1_private_widget_proto_rawDescGZIP(), []int{6}
}

func (x *PrivateWidgetsInfo) GetResults() []*PrivateWidgetInfo {
	if x != nil {
		return x.Results
	}
	return nil
}

func (x *PrivateWidgetsInfo) GetTotalCount() int32 {
	if x != nil {
		return x.TotalCount
	}
	return 0
}

var File_spaceone_api_dashboard_v1_private_widget_proto protoreflect.FileDescriptor

var file_spaceone_api_dashboard_v1_private_widget_proto_rawDesc = []byte{
	0x0a, 0x2e, 0x73, 0x70, 0x61, 0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x64,
	0x61, 0x73, 0x68, 0x62, 0x6f, 0x61, 0x72, 0x64, 0x2f, 0x76, 0x31, 0x2f, 0x70, 0x72, 0x69, 0x76,
	0x61, 0x74, 0x65, 0x5f, 0x77, 0x69, 0x64, 0x67, 0x65, 0x74, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x12, 0x19, 0x73, 0x70, 0x61, 0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x64,
	0x61, 0x73, 0x68, 0x62, 0x6f, 0x61, 0x72, 0x64, 0x2e, 0x76, 0x31, 0x1a, 0x1b, 0x67, 0x6f, 0x6f,
	0x67, 0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x65, 0x6d, 0x70,
	0x74, 0x79, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x1c, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65,
	0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x73, 0x74, 0x72, 0x75, 0x63, 0x74,
	0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x1c, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x61,
	0x70, 0x69, 0x2f, 0x61, 0x6e, 0x6e, 0x6f, 0x74, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x73, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x20, 0x73, 0x70, 0x61, 0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2f, 0x61,
	0x70, 0x69, 0x2f, 0x63, 0x6f, 0x72, 0x65, 0x2f, 0x76, 0x32, 0x2f, 0x71, 0x75, 0x65, 0x72, 0x79,
	0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0xf6, 0x01, 0x0a, 0x1a, 0x43, 0x72, 0x65, 0x61, 0x74,
	0x65, 0x50, 0x72, 0x69, 0x76, 0x61, 0x74, 0x65, 0x57, 0x69, 0x64, 0x67, 0x65, 0x74, 0x52, 0x65,
	0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x21, 0x0a, 0x0c, 0x64, 0x61, 0x73, 0x68, 0x62, 0x6f, 0x61,
	0x72, 0x64, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0b, 0x64, 0x61, 0x73,
	0x68, 0x62, 0x6f, 0x61, 0x72, 0x64, 0x49, 0x64, 0x12, 0x12, 0x0a, 0x04, 0x6e, 0x61, 0x6d, 0x65,
	0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x12, 0x20, 0x0a, 0x0b,
	0x64, 0x65, 0x73, 0x63, 0x72, 0x69, 0x70, 0x74, 0x69, 0x6f, 0x6e, 0x18, 0x03, 0x20, 0x01, 0x28,
	0x09, 0x52, 0x0b, 0x64, 0x65, 0x73, 0x63, 0x72, 0x69, 0x70, 0x74, 0x69, 0x6f, 0x6e, 0x12, 0x1f,
	0x0a, 0x0b, 0x77, 0x69, 0x64, 0x67, 0x65, 0x74, 0x5f, 0x74, 0x79, 0x70, 0x65, 0x18, 0x04, 0x20,
	0x01, 0x28, 0x09, 0x52, 0x0a, 0x77, 0x69, 0x64, 0x67, 0x65, 0x74, 0x54, 0x79, 0x70, 0x65, 0x12,
	0x31, 0x0a, 0x07, 0x6f, 0x70, 0x74, 0x69, 0x6f, 0x6e, 0x73, 0x18, 0x05, 0x20, 0x01, 0x28, 0x0b,
	0x32, 0x17, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62,
	0x75, 0x66, 0x2e, 0x53, 0x74, 0x72, 0x75, 0x63, 0x74, 0x52, 0x07, 0x6f, 0x70, 0x74, 0x69, 0x6f,
	0x6e, 0x73, 0x12, 0x2b, 0x0a, 0x04, 0x74, 0x61, 0x67, 0x73, 0x18, 0x06, 0x20, 0x01, 0x28, 0x0b,
	0x32, 0x17, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62,
	0x75, 0x66, 0x2e, 0x53, 0x74, 0x72, 0x75, 0x63, 0x74, 0x52, 0x04, 0x74, 0x61, 0x67, 0x73, 0x22,
	0xf0, 0x01, 0x0a, 0x1a, 0x55, 0x70, 0x64, 0x61, 0x74, 0x65, 0x50, 0x72, 0x69, 0x76, 0x61, 0x74,
	0x65, 0x57, 0x69, 0x64, 0x67, 0x65, 0x74, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x1b,
	0x0a, 0x09, 0x77, 0x69, 0x64, 0x67, 0x65, 0x74, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28,
	0x09, 0x52, 0x08, 0x77, 0x69, 0x64, 0x67, 0x65, 0x74, 0x49, 0x64, 0x12, 0x12, 0x0a, 0x04, 0x6e,
	0x61, 0x6d, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x12,
	0x20, 0x0a, 0x0b, 0x64, 0x65, 0x73, 0x63, 0x72, 0x69, 0x70, 0x74, 0x69, 0x6f, 0x6e, 0x18, 0x03,
	0x20, 0x01, 0x28, 0x09, 0x52, 0x0b, 0x64, 0x65, 0x73, 0x63, 0x72, 0x69, 0x70, 0x74, 0x69, 0x6f,
	0x6e, 0x12, 0x1f, 0x0a, 0x0b, 0x77, 0x69, 0x64, 0x67, 0x65, 0x74, 0x5f, 0x74, 0x79, 0x70, 0x65,
	0x18, 0x04, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0a, 0x77, 0x69, 0x64, 0x67, 0x65, 0x74, 0x54, 0x79,
	0x70, 0x65, 0x12, 0x31, 0x0a, 0x07, 0x6f, 0x70, 0x74, 0x69, 0x6f, 0x6e, 0x73, 0x18, 0x05, 0x20,
	0x01, 0x28, 0x0b, 0x32, 0x17, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x53, 0x74, 0x72, 0x75, 0x63, 0x74, 0x52, 0x07, 0x6f, 0x70,
	0x74, 0x69, 0x6f, 0x6e, 0x73, 0x12, 0x2b, 0x0a, 0x04, 0x74, 0x61, 0x67, 0x73, 0x18, 0x06, 0x20,
	0x01, 0x28, 0x0b, 0x32, 0x17, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x53, 0x74, 0x72, 0x75, 0x63, 0x74, 0x52, 0x04, 0x74, 0x61,
	0x67, 0x73, 0x22, 0x33, 0x0a, 0x14, 0x50, 0x72, 0x69, 0x76, 0x61, 0x74, 0x65, 0x57, 0x69, 0x64,
	0x67, 0x65, 0x74, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x1b, 0x0a, 0x09, 0x77, 0x69,
	0x64, 0x67, 0x65, 0x74, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x08, 0x77,
	0x69, 0x64, 0x67, 0x65, 0x74, 0x49, 0x64, 0x22, 0xa8, 0x01, 0x0a, 0x18, 0x4c, 0x6f, 0x61, 0x64,
	0x50, 0x72, 0x69, 0x76, 0x61, 0x74, 0x65, 0x57, 0x69, 0x64, 0x67, 0x65, 0x74, 0x52, 0x65, 0x71,
	0x75, 0x65, 0x73, 0x74, 0x12, 0x1b, 0x0a, 0x09, 0x77, 0x69, 0x64, 0x67, 0x65, 0x74, 0x5f, 0x69,
	0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x08, 0x77, 0x69, 0x64, 0x67, 0x65, 0x74, 0x49,
	0x64, 0x12, 0x42, 0x0a, 0x05, 0x71, 0x75, 0x65, 0x72, 0x79, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b,
	0x32, 0x2c, 0x2e, 0x73, 0x70, 0x61, 0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2e, 0x61, 0x70, 0x69, 0x2e,
	0x63, 0x6f, 0x72, 0x65, 0x2e, 0x76, 0x32, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x53, 0x65, 0x72, 0x69,
	0x65, 0x73, 0x41, 0x6e, 0x61, 0x6c, 0x79, 0x7a, 0x65, 0x51, 0x75, 0x65, 0x72, 0x79, 0x52, 0x05,
	0x71, 0x75, 0x65, 0x72, 0x79, 0x12, 0x2b, 0x0a, 0x04, 0x76, 0x61, 0x72, 0x73, 0x18, 0x03, 0x20,
	0x01, 0x28, 0x0b, 0x32, 0x17, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x53, 0x74, 0x72, 0x75, 0x63, 0x74, 0x52, 0x04, 0x76, 0x61,
	0x72, 0x73, 0x22, 0x9b, 0x01, 0x0a, 0x12, 0x50, 0x72, 0x69, 0x76, 0x61, 0x74, 0x65, 0x57, 0x69,
	0x64, 0x67, 0x65, 0x74, 0x51, 0x75, 0x65, 0x72, 0x79, 0x12, 0x31, 0x0a, 0x05, 0x71, 0x75, 0x65,
	0x72, 0x79, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1b, 0x2e, 0x73, 0x70, 0x61, 0x63, 0x65,
	0x6f, 0x6e, 0x65, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x63, 0x6f, 0x72, 0x65, 0x2e, 0x76, 0x32, 0x2e,
	0x51, 0x75, 0x65, 0x72, 0x79, 0x52, 0x05, 0x71, 0x75, 0x65, 0x72, 0x79, 0x12, 0x21, 0x0a, 0x0c,
	0x64, 0x61, 0x73, 0x68, 0x62, 0x6f, 0x61, 0x72, 0x64, 0x5f, 0x69, 0x64, 0x18, 0x02, 0x20, 0x01,
	0x28, 0x09, 0x52, 0x0b, 0x64, 0x61, 0x73, 0x68, 0x62, 0x6f, 0x61, 0x72, 0x64, 0x49, 0x64, 0x12,
	0x1b, 0x0a, 0x09, 0x77, 0x69, 0x64, 0x67, 0x65, 0x74, 0x5f, 0x69, 0x64, 0x18, 0x03, 0x20, 0x01,
	0x28, 0x09, 0x52, 0x08, 0x77, 0x69, 0x64, 0x67, 0x65, 0x74, 0x49, 0x64, 0x12, 0x12, 0x0a, 0x04,
	0x6e, 0x61, 0x6d, 0x65, 0x18, 0x04, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x6e, 0x61, 0x6d, 0x65,
	0x22, 0xfe, 0x02, 0x0a, 0x11, 0x50, 0x72, 0x69, 0x76, 0x61, 0x74, 0x65, 0x57, 0x69, 0x64, 0x67,
	0x65, 0x74, 0x49, 0x6e, 0x66, 0x6f, 0x12, 0x1b, 0x0a, 0x09, 0x77, 0x69, 0x64, 0x67, 0x65, 0x74,
	0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x08, 0x77, 0x69, 0x64, 0x67, 0x65,
	0x74, 0x49, 0x64, 0x12, 0x12, 0x0a, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28,
	0x09, 0x52, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x12, 0x20, 0x0a, 0x0b, 0x64, 0x65, 0x73, 0x63, 0x72,
	0x69, 0x70, 0x74, 0x69, 0x6f, 0x6e, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0b, 0x64, 0x65,
	0x73, 0x63, 0x72, 0x69, 0x70, 0x74, 0x69, 0x6f, 0x6e, 0x12, 0x1f, 0x0a, 0x0b, 0x77, 0x69, 0x64,
	0x67, 0x65, 0x74, 0x5f, 0x74, 0x79, 0x70, 0x65, 0x18, 0x04, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0a,
	0x77, 0x69, 0x64, 0x67, 0x65, 0x74, 0x54, 0x79, 0x70, 0x65, 0x12, 0x31, 0x0a, 0x07, 0x6f, 0x70,
	0x74, 0x69, 0x6f, 0x6e, 0x73, 0x18, 0x05, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x17, 0x2e, 0x67, 0x6f,
	0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x53, 0x74,
	0x72, 0x75, 0x63, 0x74, 0x52, 0x07, 0x6f, 0x70, 0x74, 0x69, 0x6f, 0x6e, 0x73, 0x12, 0x2b, 0x0a,
	0x04, 0x74, 0x61, 0x67, 0x73, 0x18, 0x06, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x17, 0x2e, 0x67, 0x6f,
	0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x53, 0x74,
	0x72, 0x75, 0x63, 0x74, 0x52, 0x04, 0x74, 0x61, 0x67, 0x73, 0x12, 0x1b, 0x0a, 0x09, 0x64, 0x6f,
	0x6d, 0x61, 0x69, 0x6e, 0x5f, 0x69, 0x64, 0x18, 0x15, 0x20, 0x01, 0x28, 0x09, 0x52, 0x08, 0x64,
	0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x49, 0x64, 0x12, 0x17, 0x0a, 0x07, 0x75, 0x73, 0x65, 0x72, 0x5f,
	0x69, 0x64, 0x18, 0x16, 0x20, 0x01, 0x28, 0x09, 0x52, 0x06, 0x75, 0x73, 0x65, 0x72, 0x49, 0x64,
	0x12, 0x21, 0x0a, 0x0c, 0x64, 0x61, 0x73, 0x68, 0x62, 0x6f, 0x61, 0x72, 0x64, 0x5f, 0x69, 0x64,
	0x18, 0x17, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0b, 0x64, 0x61, 0x73, 0x68, 0x62, 0x6f, 0x61, 0x72,
	0x64, 0x49, 0x64, 0x12, 0x1d, 0x0a, 0x0a, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65, 0x64, 0x5f, 0x61,
	0x74, 0x18, 0x1f, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65, 0x64,
	0x41, 0x74, 0x12, 0x1d, 0x0a, 0x0a, 0x75, 0x70, 0x64, 0x61, 0x74, 0x65, 0x64, 0x5f, 0x61, 0x74,
	0x18, 0x20, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09, 0x75, 0x70, 0x64, 0x61, 0x74, 0x65, 0x64, 0x41,
	0x74, 0x22, 0x7d, 0x0a, 0x12, 0x50, 0x72, 0x69, 0x76, 0x61, 0x74, 0x65, 0x57, 0x69, 0x64, 0x67,
	0x65, 0x74, 0x73, 0x49, 0x6e, 0x66, 0x6f, 0x12, 0x46, 0x0a, 0x07, 0x72, 0x65, 0x73, 0x75, 0x6c,
	0x74, 0x73, 0x18, 0x01, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x2c, 0x2e, 0x73, 0x70, 0x61, 0x63, 0x65,
	0x6f, 0x6e, 0x65, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x64, 0x61, 0x73, 0x68, 0x62, 0x6f, 0x61, 0x72,
	0x64, 0x2e, 0x76, 0x31, 0x2e, 0x50, 0x72, 0x69, 0x76, 0x61, 0x74, 0x65, 0x57, 0x69, 0x64, 0x67,
	0x65, 0x74, 0x49, 0x6e, 0x66, 0x6f, 0x52, 0x07, 0x72, 0x65, 0x73, 0x75, 0x6c, 0x74, 0x73, 0x12,
	0x1f, 0x0a, 0x0b, 0x74, 0x6f, 0x74, 0x61, 0x6c, 0x5f, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x18, 0x02,
	0x20, 0x01, 0x28, 0x05, 0x52, 0x0a, 0x74, 0x6f, 0x74, 0x61, 0x6c, 0x43, 0x6f, 0x75, 0x6e, 0x74,
	0x32, 0xed, 0x06, 0x0a, 0x0d, 0x50, 0x72, 0x69, 0x76, 0x61, 0x74, 0x65, 0x57, 0x69, 0x64, 0x67,
	0x65, 0x74, 0x12, 0x9a, 0x01, 0x0a, 0x06, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65, 0x12, 0x35, 0x2e,
	0x73, 0x70, 0x61, 0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x64, 0x61, 0x73,
	0x68, 0x62, 0x6f, 0x61, 0x72, 0x64, 0x2e, 0x76, 0x31, 0x2e, 0x43, 0x72, 0x65, 0x61, 0x74, 0x65,
	0x50, 0x72, 0x69, 0x76, 0x61, 0x74, 0x65, 0x57, 0x69, 0x64, 0x67, 0x65, 0x74, 0x52, 0x65, 0x71,
	0x75, 0x65, 0x73, 0x74, 0x1a, 0x2c, 0x2e, 0x73, 0x70, 0x61, 0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2e,
	0x61, 0x70, 0x69, 0x2e, 0x64, 0x61, 0x73, 0x68, 0x62, 0x6f, 0x61, 0x72, 0x64, 0x2e, 0x76, 0x31,
	0x2e, 0x50, 0x72, 0x69, 0x76, 0x61, 0x74, 0x65, 0x57, 0x69, 0x64, 0x67, 0x65, 0x74, 0x49, 0x6e,
	0x66, 0x6f, 0x22, 0x2b, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x25, 0x3a, 0x01, 0x2a, 0x22, 0x20, 0x2f,
	0x77, 0x69, 0x64, 0x67, 0x65, 0x74, 0x2f, 0x76, 0x31, 0x2f, 0x70, 0x72, 0x69, 0x76, 0x61, 0x74,
	0x65, 0x2d, 0x77, 0x69, 0x64, 0x67, 0x65, 0x74, 0x2f, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65, 0x12,
	0x9a, 0x01, 0x0a, 0x06, 0x75, 0x70, 0x64, 0x61, 0x74, 0x65, 0x12, 0x35, 0x2e, 0x73, 0x70, 0x61,
	0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x64, 0x61, 0x73, 0x68, 0x62, 0x6f,
	0x61, 0x72, 0x64, 0x2e, 0x76, 0x31, 0x2e, 0x55, 0x70, 0x64, 0x61, 0x74, 0x65, 0x50, 0x72, 0x69,
	0x76, 0x61, 0x74, 0x65, 0x57, 0x69, 0x64, 0x67, 0x65, 0x74, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73,
	0x74, 0x1a, 0x2c, 0x2e, 0x73, 0x70, 0x61, 0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2e, 0x61, 0x70, 0x69,
	0x2e, 0x64, 0x61, 0x73, 0x68, 0x62, 0x6f, 0x61, 0x72, 0x64, 0x2e, 0x76, 0x31, 0x2e, 0x50, 0x72,
	0x69, 0x76, 0x61, 0x74, 0x65, 0x57, 0x69, 0x64, 0x67, 0x65, 0x74, 0x49, 0x6e, 0x66, 0x6f, 0x22,
	0x2b, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x25, 0x3a, 0x01, 0x2a, 0x22, 0x20, 0x2f, 0x77, 0x69, 0x64,
	0x67, 0x65, 0x74, 0x2f, 0x76, 0x31, 0x2f, 0x70, 0x72, 0x69, 0x76, 0x61, 0x74, 0x65, 0x2d, 0x77,
	0x69, 0x64, 0x67, 0x65, 0x74, 0x2f, 0x75, 0x70, 0x64, 0x61, 0x74, 0x65, 0x12, 0x7e, 0x0a, 0x06,
	0x64, 0x65, 0x6c, 0x65, 0x74, 0x65, 0x12, 0x2f, 0x2e, 0x73, 0x70, 0x61, 0x63, 0x65, 0x6f, 0x6e,
	0x65, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x64, 0x61, 0x73, 0x68, 0x62, 0x6f, 0x61, 0x72, 0x64, 0x2e,
	0x76, 0x31, 0x2e, 0x50, 0x72, 0x69, 0x76, 0x61, 0x74, 0x65, 0x57, 0x69, 0x64, 0x67, 0x65, 0x74,
	0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x16, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65,
	0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x45, 0x6d, 0x70, 0x74, 0x79, 0x22,
	0x2b, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x25, 0x3a, 0x01, 0x2a, 0x22, 0x20, 0x2f, 0x77, 0x69, 0x64,
	0x67, 0x65, 0x74, 0x2f, 0x76, 0x31, 0x2f, 0x70, 0x72, 0x69, 0x76, 0x61, 0x74, 0x65, 0x2d, 0x77,
	0x69, 0x64, 0x67, 0x65, 0x74, 0x2f, 0x64, 0x65, 0x6c, 0x65, 0x74, 0x65, 0x12, 0x7f, 0x0a, 0x04,
	0x6c, 0x6f, 0x61, 0x64, 0x12, 0x33, 0x2e, 0x73, 0x70, 0x61, 0x63, 0x65, 0x6f, 0x6e, 0x65, 0x2e,
	0x61, 0x70, 0x69, 0x2e, 0x64, 0x61, 0x73, 0x68, 0x62, 0x6f, 0x61, 0x72, 0x64, 0x2e, 0x76, 0x31,
	0x2e, 0x4c, 0x6f, 0x61, 0x64, 0x50, 0x72, 0x69, 0x76, 0x61, 0x74, 0x65, 0x57, 0x69, 0x64, 0x67,
	0x65, 0x74, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x17, 0x2e, 0x67, 0x6f, 0x6f, 0x67,
	0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x53, 0x74, 0x72, 0x75,
	0x63, 0x74, 0x22, 0x29, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x23, 0x3a, 0x01, 0x2a, 0x22, 0x1e, 0x2f,
	0x77, 0x69, 0x64, 0x67, 0x65, 0x74, 0x2f, 0x76, 0x31, 0x2f, 0x70, 0x72, 0x69, 0x76, 0x61, 0x74,
	0x65, 0x2d, 0x77, 0x69, 0x64, 0x67, 0x65, 0x74, 0x2f, 0x6c, 0x6f, 0x61, 0x64, 0x12, 0x8e, 0x01,
	0x0a, 0x03, 0x67, 0x65, 0x74, 0x12, 0x2f, 0x2e, 0x73, 0x70, 0x61, 0x63, 0x65, 0x6f, 0x6e, 0x65,
	0x2e, 0x61, 0x70, 0x69, 0x2e, 0x64, 0x61, 0x73, 0x68, 0x62, 0x6f, 0x61, 0x72, 0x64, 0x2e, 0x76,
	0x31, 0x2e, 0x50, 0x72, 0x69, 0x76, 0x61, 0x74, 0x65, 0x57, 0x69, 0x64, 0x67, 0x65, 0x74, 0x52,
	0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x2c, 0x2e, 0x73, 0x70, 0x61, 0x63, 0x65, 0x6f, 0x6e,
	0x65, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x64, 0x61, 0x73, 0x68, 0x62, 0x6f, 0x61, 0x72, 0x64, 0x2e,
	0x76, 0x31, 0x2e, 0x50, 0x72, 0x69, 0x76, 0x61, 0x74, 0x65, 0x57, 0x69, 0x64, 0x67, 0x65, 0x74,
	0x49, 0x6e, 0x66, 0x6f, 0x22, 0x28, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x22, 0x3a, 0x01, 0x2a, 0x22,
	0x1d, 0x2f, 0x77, 0x69, 0x64, 0x67, 0x65, 0x74, 0x2f, 0x76, 0x31, 0x2f, 0x70, 0x72, 0x69, 0x76,
	0x61, 0x74, 0x65, 0x2d, 0x77, 0x69, 0x64, 0x67, 0x65, 0x74, 0x2f, 0x67, 0x65, 0x74, 0x12, 0x8f,
	0x01, 0x0a, 0x04, 0x6c, 0x69, 0x73, 0x74, 0x12, 0x2d, 0x2e, 0x73, 0x70, 0x61, 0x63, 0x65, 0x6f,
	0x6e, 0x65, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x64, 0x61, 0x73, 0x68, 0x62, 0x6f, 0x61, 0x72, 0x64,
	0x2e, 0x76, 0x31, 0x2e, 0x50, 0x72, 0x69, 0x76, 0x61, 0x74, 0x65, 0x57, 0x69, 0x64, 0x67, 0x65,
	0x74, 0x51, 0x75, 0x65, 0x72, 0x79, 0x1a, 0x2d, 0x2e, 0x73, 0x70, 0x61, 0x63, 0x65, 0x6f, 0x6e,
	0x65, 0x2e, 0x61, 0x70, 0x69, 0x2e, 0x64, 0x61, 0x73, 0x68, 0x62, 0x6f, 0x61, 0x72, 0x64, 0x2e,
	0x76, 0x31, 0x2e, 0x50, 0x72, 0x69, 0x76, 0x61, 0x74, 0x65, 0x57, 0x69, 0x64, 0x67, 0x65, 0x74,
	0x73, 0x49, 0x6e, 0x66, 0x6f, 0x22, 0x29, 0x82, 0xd3, 0xe4, 0x93, 0x02, 0x23, 0x3a, 0x01, 0x2a,
	0x22, 0x1e, 0x2f, 0x77, 0x69, 0x64, 0x67, 0x65, 0x74, 0x2f, 0x76, 0x31, 0x2f, 0x70, 0x72, 0x69,
	0x76, 0x61, 0x74, 0x65, 0x2d, 0x77, 0x69, 0x64, 0x67, 0x65, 0x74, 0x2f, 0x6c, 0x69, 0x73, 0x74,
	0x42, 0x40, 0x5a, 0x3e, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x63,
	0x6c, 0x6f, 0x75, 0x64, 0x66, 0x6f, 0x72, 0x65, 0x74, 0x2d, 0x69, 0x6f, 0x2f, 0x61, 0x70, 0x69,
	0x2f, 0x64, 0x69, 0x73, 0x74, 0x2f, 0x67, 0x6f, 0x2f, 0x73, 0x70, 0x61, 0x63, 0x65, 0x6f, 0x6e,
	0x65, 0x2f, 0x61, 0x70, 0x69, 0x2f, 0x64, 0x61, 0x73, 0x68, 0x62, 0x6f, 0x61, 0x72, 0x64, 0x2f,
	0x76, 0x31, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_spaceone_api_dashboard_v1_private_widget_proto_rawDescOnce sync.Once
	file_spaceone_api_dashboard_v1_private_widget_proto_rawDescData = file_spaceone_api_dashboard_v1_private_widget_proto_rawDesc
)

func file_spaceone_api_dashboard_v1_private_widget_proto_rawDescGZIP() []byte {
	file_spaceone_api_dashboard_v1_private_widget_proto_rawDescOnce.Do(func() {
		file_spaceone_api_dashboard_v1_private_widget_proto_rawDescData = protoimpl.X.CompressGZIP(file_spaceone_api_dashboard_v1_private_widget_proto_rawDescData)
	})
	return file_spaceone_api_dashboard_v1_private_widget_proto_rawDescData
}

var file_spaceone_api_dashboard_v1_private_widget_proto_msgTypes = make([]protoimpl.MessageInfo, 7)
var file_spaceone_api_dashboard_v1_private_widget_proto_goTypes = []interface{}{
	(*CreatePrivateWidgetRequest)(nil), // 0: spaceone.api.dashboard.v1.CreatePrivateWidgetRequest
	(*UpdatePrivateWidgetRequest)(nil), // 1: spaceone.api.dashboard.v1.UpdatePrivateWidgetRequest
	(*PrivateWidgetRequest)(nil),       // 2: spaceone.api.dashboard.v1.PrivateWidgetRequest
	(*LoadPrivateWidgetRequest)(nil),   // 3: spaceone.api.dashboard.v1.LoadPrivateWidgetRequest
	(*PrivateWidgetQuery)(nil),         // 4: spaceone.api.dashboard.v1.PrivateWidgetQuery
	(*PrivateWidgetInfo)(nil),          // 5: spaceone.api.dashboard.v1.PrivateWidgetInfo
	(*PrivateWidgetsInfo)(nil),         // 6: spaceone.api.dashboard.v1.PrivateWidgetsInfo
	(*_struct.Struct)(nil),             // 7: google.protobuf.Struct
	(*v2.TimeSeriesAnalyzeQuery)(nil),  // 8: spaceone.api.core.v2.TimeSeriesAnalyzeQuery
	(*v2.Query)(nil),                   // 9: spaceone.api.core.v2.Query
	(*empty.Empty)(nil),                // 10: google.protobuf.Empty
}
var file_spaceone_api_dashboard_v1_private_widget_proto_depIdxs = []int32{
	7,  // 0: spaceone.api.dashboard.v1.CreatePrivateWidgetRequest.options:type_name -> google.protobuf.Struct
	7,  // 1: spaceone.api.dashboard.v1.CreatePrivateWidgetRequest.tags:type_name -> google.protobuf.Struct
	7,  // 2: spaceone.api.dashboard.v1.UpdatePrivateWidgetRequest.options:type_name -> google.protobuf.Struct
	7,  // 3: spaceone.api.dashboard.v1.UpdatePrivateWidgetRequest.tags:type_name -> google.protobuf.Struct
	8,  // 4: spaceone.api.dashboard.v1.LoadPrivateWidgetRequest.query:type_name -> spaceone.api.core.v2.TimeSeriesAnalyzeQuery
	7,  // 5: spaceone.api.dashboard.v1.LoadPrivateWidgetRequest.vars:type_name -> google.protobuf.Struct
	9,  // 6: spaceone.api.dashboard.v1.PrivateWidgetQuery.query:type_name -> spaceone.api.core.v2.Query
	7,  // 7: spaceone.api.dashboard.v1.PrivateWidgetInfo.options:type_name -> google.protobuf.Struct
	7,  // 8: spaceone.api.dashboard.v1.PrivateWidgetInfo.tags:type_name -> google.protobuf.Struct
	5,  // 9: spaceone.api.dashboard.v1.PrivateWidgetsInfo.results:type_name -> spaceone.api.dashboard.v1.PrivateWidgetInfo
	0,  // 10: spaceone.api.dashboard.v1.PrivateWidget.create:input_type -> spaceone.api.dashboard.v1.CreatePrivateWidgetRequest
	1,  // 11: spaceone.api.dashboard.v1.PrivateWidget.update:input_type -> spaceone.api.dashboard.v1.UpdatePrivateWidgetRequest
	2,  // 12: spaceone.api.dashboard.v1.PrivateWidget.delete:input_type -> spaceone.api.dashboard.v1.PrivateWidgetRequest
	3,  // 13: spaceone.api.dashboard.v1.PrivateWidget.load:input_type -> spaceone.api.dashboard.v1.LoadPrivateWidgetRequest
	2,  // 14: spaceone.api.dashboard.v1.PrivateWidget.get:input_type -> spaceone.api.dashboard.v1.PrivateWidgetRequest
	4,  // 15: spaceone.api.dashboard.v1.PrivateWidget.list:input_type -> spaceone.api.dashboard.v1.PrivateWidgetQuery
	5,  // 16: spaceone.api.dashboard.v1.PrivateWidget.create:output_type -> spaceone.api.dashboard.v1.PrivateWidgetInfo
	5,  // 17: spaceone.api.dashboard.v1.PrivateWidget.update:output_type -> spaceone.api.dashboard.v1.PrivateWidgetInfo
	10, // 18: spaceone.api.dashboard.v1.PrivateWidget.delete:output_type -> google.protobuf.Empty
	7,  // 19: spaceone.api.dashboard.v1.PrivateWidget.load:output_type -> google.protobuf.Struct
	5,  // 20: spaceone.api.dashboard.v1.PrivateWidget.get:output_type -> spaceone.api.dashboard.v1.PrivateWidgetInfo
	6,  // 21: spaceone.api.dashboard.v1.PrivateWidget.list:output_type -> spaceone.api.dashboard.v1.PrivateWidgetsInfo
	16, // [16:22] is the sub-list for method output_type
	10, // [10:16] is the sub-list for method input_type
	10, // [10:10] is the sub-list for extension type_name
	10, // [10:10] is the sub-list for extension extendee
	0,  // [0:10] is the sub-list for field type_name
}

func init() { file_spaceone_api_dashboard_v1_private_widget_proto_init() }
func file_spaceone_api_dashboard_v1_private_widget_proto_init() {
	if File_spaceone_api_dashboard_v1_private_widget_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_spaceone_api_dashboard_v1_private_widget_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*CreatePrivateWidgetRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_spaceone_api_dashboard_v1_private_widget_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*UpdatePrivateWidgetRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_spaceone_api_dashboard_v1_private_widget_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*PrivateWidgetRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_spaceone_api_dashboard_v1_private_widget_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*LoadPrivateWidgetRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_spaceone_api_dashboard_v1_private_widget_proto_msgTypes[4].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*PrivateWidgetQuery); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_spaceone_api_dashboard_v1_private_widget_proto_msgTypes[5].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*PrivateWidgetInfo); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_spaceone_api_dashboard_v1_private_widget_proto_msgTypes[6].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*PrivateWidgetsInfo); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_spaceone_api_dashboard_v1_private_widget_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   7,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_spaceone_api_dashboard_v1_private_widget_proto_goTypes,
		DependencyIndexes: file_spaceone_api_dashboard_v1_private_widget_proto_depIdxs,
		MessageInfos:      file_spaceone_api_dashboard_v1_private_widget_proto_msgTypes,
	}.Build()
	File_spaceone_api_dashboard_v1_private_widget_proto = out.File
	file_spaceone_api_dashboard_v1_private_widget_proto_rawDesc = nil
	file_spaceone_api_dashboard_v1_private_widget_proto_goTypes = nil
	file_spaceone_api_dashboard_v1_private_widget_proto_depIdxs = nil
}
