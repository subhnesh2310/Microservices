from rest_framework import serializers
import hashlib
from pixi_db.sqlalchemy_models import SQLAlchemyConnectNE, SQLAlchemyDisconnectNE, TestExecution, Users, TestStepsResults, TestExecutionMetrics, TestMetadataTable

class ConnectNESerializer(serializers.Serializer):
    connect_ne_uuid = serializers.CharField(max_length=150)
    handle = serializers.CharField(max_length=100)
    username = serializers.CharField(max_length=100, default="temp")
    password = serializers.CharField(write_only=True, max_length=164)
    hostname = serializers.CharField(max_length=100)
    port = serializers.IntegerField(default=22)
    interface = serializers.CharField(max_length=50, default="CLI")
    created_time = serializers.DateTimeField(read_only=True)
    connection_status = serializers.CharField(max_length=1, default="p")

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = SQLAlchemyConnectNE(**validated_data)
        if password:
            instance.set_password(password)
        return instance  # Return the instance without saving

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for key, value in validated_data.items():
            setattr(instance, key, value)
        if password:
            instance.set_password(password)
        return instance  # Return the instance without saving
    

class DisconnectNESerializer(serializers.Serializer):
    disconnect_ne_uuid = serializers.CharField(max_length=150)
    handle = serializers.CharField(max_length=100)
    username = serializers.CharField(max_length=100, default="temp")
    password = serializers.CharField(write_only=True, max_length=64)
    hostname = serializers.CharField(max_length=100)
    port = serializers.IntegerField(default=22)
    interface = serializers.CharField(max_length=50, default="CLI")
    created_time = serializers.DateTimeField(read_only=True)
    disconnect_status = serializers.CharField(max_length=1, default="p")

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = SQLAlchemyDisconnectNE(**validated_data)
        if password:
            instance.set_password(password)
        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for key, value in validated_data.items():
            setattr(instance, key, value)
        if password:
            instance.set_password(password)
        return instance


class TestExecutionSerializer(serializers.Serializer):
    execution_uuid = serializers.CharField(max_length=50)
    environment_details = serializers.CharField(max_length=255)
    userid_uuid = serializers.CharField(max_length=50)
    test_suite_uuid = serializers.IntegerField()
    test_suite_name = serializers.CharField(max_length=100)
    test_case_uuid = serializers.IntegerField()
    test_case_name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField(read_only=True)
    executed_at = serializers.DateTimeField()
    start_at = serializers.DateTimeField()
    end_at = serializers.DateTimeField()
    time_taken = serializers.CharField(max_length=20)
    result = serializers.CharField(max_length=20)
    sw_package = serializers.CharField(max_length=100)
    logs_path = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return TestExecution(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        return instance


class UsersSerializer(serializers.Serializer):
    userid_uuid = serializers.CharField(max_length=50)
    email_id = serializers.EmailField(max_length=100)
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=64, write_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    role_uuid = serializers.IntegerField()
    role_name = serializers.CharField(source='role.role_name', read_only=True)
    permission_uuid = serializers.CharField(max_length=150)
    permission_name = serializers.CharField(source='permission.permission_name', read_only=True)
    csim_status = serializers.CharField(max_length=20)

    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = Users(**validated_data)
        instance.set_password(password)
        return instance

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data.pop('password'))
        for key, value in validated_data.items():
            setattr(instance, key, value)
        return instance


class TestStepsResultsSerializer(serializers.Serializer):
    log_id_uuid = serializers.CharField(max_length=50)
    log_path = serializers.CharField(max_length=255)
    execution_uuid = serializers.CharField(max_length=50)
    test_result_status = serializers.CharField(max_length=1)
    created_at = serializers.DateTimeField(read_only=True)
    test_suite_uuid = serializers.CharField(max_length=150)
    userid_uuid = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return TestStepsResults(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        return instance


class TestExecutionMetricsSerializer(serializers.Serializer):
    matric_uuid = serializers.CharField(max_length=50)
    execution_uuid = serializers.CharField(max_length=50)
    execution_table = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField(read_only=True)
    execution_count = serializers.IntegerField()
    each_execution_status = serializers.JSONField()

    def create(self, validated_data):
        return TestExecutionMetrics(**validated_data)

    def update(self, instance, validated_data):
        instance.execution_uuid = validated_data.get('execution_uuid', instance.execution_uuid)
        instance.execution_table = validated_data.get('execution_table', instance.execution_table)
        instance.execution_count = validated_data.get('execution_count', instance.execution_count)
        instance.each_execution_status = validated_data.get('each_execution_status', instance.each_execution_status)
        return instance

class TestStepsResultsSerializer(serializers.Serializer):
    log_id_uuid = serializers.CharField(max_length=50)
    log_path = serializers.CharField(max_length=255)
    execution_uuid = serializers.CharField(max_length=50)
    test_result_status = serializers.CharField(max_length=1)
    created_at = serializers.DateTimeField(read_only=True)
    test_suite_uuid = serializers.CharField(max_length=150)
    userid_uuid = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return TestStepsResults(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        return instance
    

class TestMetadataSerializer(serializers.Serializer):
    metadata_uuid = serializers.CharField(max_length=50)
    owner = serializers.CharField(max_length=255)
    doa = serializers.CharField(max_length=20)
    with_tgen = serializers.CharField(max_length=3)
    status = serializers.CharField(max_length=20)
    product = serializers.CharField(max_length=50)
    interface = serializers.CharField(max_length=50)
    script_id = serializers.CharField(max_length=10)
    title = serializers.CharField(max_length=255)
    software_version = serializers.CharField(max_length=20)
    simulator_compatible = serializers.CharField(max_length=3)


    def create(self, validated_data):
        return TestMetadataTable(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        return instance



# class SendRCVSerializer(serializers.Serializer):

#     sendRcv_uuid = serializers.CharField(max_length=150)
#     handle = serializers.CharField(max_length=100)
#     command = serializers.CharField(max_length=500)

#     def create(self, validated_data):
#         return SQLAlchemySendRCV(**validated_data)

#     def update(self, instance, validated_data):
#         for attr, value in validated_data.items():
#             setattr(instance, attr, value)
#         return instance


# class ComparePair_Serializer(serializers.Serializer):
#     compare_pair_uuid = serializers.CharField(max_length=150)
#     stash = serializers.CharField(max_length=100)
#     compare_input = serializers.CharField(max_length=250)
#     compare_result = serializers.CharField(max_length=250)

#     def create(self, validated_data):
#         return SQLAlchemyComparePairs(**validated_data)

#     def update(self, instance, validated_data):
#         for attr, value in validated_data.items():
#             setattr(instance, attr, value)
#         return instance
    

# class CPixiUserTableSerializer(serializers.Serializer):
#     uuid = serializers.CharField(max_length=150, read_only=True)
#     username = serializers.CharField(max_length=100)
#     filename1 = serializers.CharField(max_length=255)
#     file1path = serializers.CharField(max_length=255)
#     filename2 = serializers.CharField(max_length=255)
#     file2path = serializers.CharField(max_length=255)

#     def create(self, validated_data):
#         return CPixiUserTable(**validated_data)

#     def update(self, instance, validated_data):
#         instance.username = validated_data.get('username', instance.username)
#         instance.filename1 = validated_data.get('filename1', instance.filename1)
#         instance.file1path = validated_data.get('file1path', instance.file1path)
#         instance.filename2 = validated_data.get('filename2', instance.filename2)
#         instance.file2path = validated_data.get('file2path', instance.file2path)
#         return instance
