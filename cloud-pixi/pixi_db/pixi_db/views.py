from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from sqlalchemy.orm import sessionmaker
from pixi_db import sqlalchemy_models
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from pixi_db.sqlalchemy_models import SQLAlchemyConnectNE, SQLAlchemyDisconnectNE, TestExecution, Users, TestStepsResults, TestExecutionMetrics, TestMetadataTable
from pixi_db.serializers import ConnectNESerializer, DisconnectNESerializer, TestExecutionSerializer, UsersSerializer, TestStepsResultsSerializer, TestExecutionMetricsSerializer, TestMetadataSerializer

Session = sessionmaker(bind=sqlalchemy_models.engine)

class SQLAlchemyConnectNEAPIView(APIView):
    def get(self, request, pk=None):
        session = Session()
        try:
            if pk:
                instance = session.query(SQLAlchemyConnectNE).filter_by(connect_ne_uuid=pk).first()
                serializer = ConnectNESerializer(instance)
            else:
                queryset = session.query(SQLAlchemyConnectNE).all()
                serializer = ConnectNESerializer(queryset, many=True)
            return Response(serializer.data)
        finally:
            session.close()

    def post(self, request):
        serializer = ConnectNESerializer(data=request.data)
        if serializer.is_valid():
            session = Session()
            try:
                instance = serializer.create(serializer.validated_data)
                session.add(instance)  # Add instance to session
                session.commit()  # Commit changes to database
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            finally:
                session.close()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        session = Session()
        try:
            instance = session.query(SQLAlchemyConnectNE).filter_by(connect_ne_uuid=pk).first()
            if instance:
                serializer = ConnectNESerializer(instance, data=request.data)
                if serializer.is_valid():
                    serializer.update(instance, serializer.validated_data)
                    session.commit()  # Commit changes
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_404_NOT_FOUND)
        finally:
            session.close()

    def delete(self, request, pk):
        session = Session()
        try:
            instance = session.query(SQLAlchemyConnectNE).filter_by(connect_ne_uuid=pk).first()
            if instance:
                session.delete(instance)
                session.commit()  # Commit deletion
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(status=status.HTTP_404_NOT_FOUND)
        finally:
            session.close()

class SQLAlchemyDisconnectNEAPIView(APIView):
    def get(self, request, pk=None):
        session = Session()
        try:
            if pk:
                instance = session.query(SQLAlchemyDisconnectNE).filter_by(disconnect_ne_uuid=pk).first()
                serializer = DisconnectNESerializer(instance)
            else:
                queryset = session.query(SQLAlchemyDisconnectNE).all()
                serializer = DisconnectNESerializer(queryset, many=True)
            return Response(serializer.data)
        finally:
            session.close()

    def post(self, request):
        serializer = DisconnectNESerializer(data=request.data)
        if serializer.is_valid():
            session = Session()
            try:
                instance = serializer.create(serializer.validated_data)
                session.add(instance)
                session.commit()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            finally:
                session.close()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        session = Session()
        try:
            instance = session.query(SQLAlchemyDisconnectNE).filter_by(disconnect_ne_uuid=pk).first()
            if instance:
                serializer = DisconnectNESerializer(instance, data=request.data)
                if serializer.is_valid():
                    serializer.update(instance, serializer.validated_data)
                    session.commit()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_404_NOT_FOUND)
        finally:
            session.close()

    def delete(self, request, pk):
        session = Session()
        try:
            instance = session.query(SQLAlchemyDisconnectNE).filter_by(disconnect_ne_uuid=pk).first()
            if instance:
                session.delete(instance)
                session.commit()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(status=status.HTTP_404_NOT_FOUND)
        finally:
            session.close()


class TestExecutionAPIView(APIView):
    def get(self, request, pk=None):
        session = Session()
        try:
            if pk:
                instance = session.query(TestExecution).filter_by(execution_uuid=pk).first()
                serializer = TestExecutionSerializer(instance)
            else:
                queryset = session.query(TestExecution).all()
                serializer = TestExecutionSerializer(queryset, many=True)
            return Response(serializer.data)
        finally:
            session.close()

    def post(self, request):
        serializer = TestExecutionSerializer(data=request.data)
        if serializer.is_valid():
            session = Session()
            try:
                instance = serializer.create(serializer.validated_data)
                session.add(instance)
                session.commit()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            finally:
                session.close()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        session = Session()
        try:
            instance = session.query(TestExecution).filter_by(execution_uuid=pk).first()
            if instance:
                serializer = TestExecutionSerializer(instance, data=request.data)
                if serializer.is_valid():
                    serializer.update(instance, serializer.validated_data)
                    session.commit()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_404_NOT_FOUND)
        finally:
            session.close()

    def delete(self, request, pk):
        session = Session()
        try:
            instance = session.query(TestExecution).filter_by(execution_uuid=pk).first()
            if instance:
                session.delete(instance)
                session.commit()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(status=status.HTTP_404_NOT_FOUND)
        finally:
            session.close()


class UsersAPIView(APIView):
    def get(self, request, pk=None):
        session = Session()
        try:
            if pk:
                instance = session.query(Users).filter_by(userid_uuid=pk).first()
                serializer = UsersSerializer(instance)
            else:
                queryset = session.query(Users).all()
                serializer = UsersSerializer(queryset, many=True)
            return Response(serializer.data)
        finally:
            session.close()

    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            session = Session()
            try:
                instance = serializer.create(serializer.validated_data)
                session.add(instance)
                session.commit()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            finally:
                session.close()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        session = Session()
        try:
            instance = session.query(Users).filter_by(userid_uuid=pk).first()
            if instance:
                serializer = UsersSerializer(instance, data=request.data)
                if serializer.is_valid():
                    serializer.update(instance, serializer.validated_data)
                    session.commit()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_404_NOT_FOUND)
        finally:
            session.close()

    def delete(self, request, pk):
        session = Session()
        try:
            instance = session.query(Users).filter_by(userid_uuid=pk).first()
            if instance:
                session.delete(instance)
                session.commit()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(status=status.HTTP_404_NOT_FOUND)
        finally:
            session.close()


class TestStepsResultsAPIView(APIView):
    def get(self, request, log_id=None):
        session = Session()
        if log_id:
            try:
                instance = session.query(TestStepsResults).filter_by(log_id_uuid=log_id).first()
                serializer = TestStepsResultsSerializer(instance)
                return Response(serializer.data)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        else:
            queryset = session.query(TestStepsResults).all()
            serializer = TestStepsResultsSerializer(queryset, many=True)
            return Response(serializer.data)

    def post(self, request):
        session = Session()
        serializer = TestStepsResultsSerializer(data=request.data)
        if serializer.is_valid():
            try:
                instance = serializer.create(serializer.validated_data)
                session.add(instance)
                session.commit()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                session.rollback()
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, log_id):
        session = Session()
        try:
            instance = session.query(TestStepsResults).filter_by(log_id_uuid=log_id).first()
            if instance:
                serializer = TestStepsResultsSerializer(instance, data=request.data)
                if serializer.is_valid():
                    serializer.update(instance, serializer.validated_data)
                    session.commit()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            session.rollback()
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, log_id):
        session = Session()
        try:
            instance = session.query(TestStepsResults).filter_by(log_id_uuid=log_id).first()
            if instance:
                session.delete(instance)
                session.commit()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            session.rollback()
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

class TestExecutionMetricsAPIView(APIView):
    def get(self, request, pk=None):
        session = Session()
        try:
            if pk:
                instance = session.query(TestExecutionMetrics).filter_by(matric_uuid=pk).first()
                serializer = TestExecutionMetricsSerializer(instance)
            else:
                queryset = session.query(TestExecutionMetrics).all()
                serializer = TestExecutionMetricsSerializer(queryset, many=True)
            return Response(serializer.data)
        finally:
            session.close()

    def post(self, request):
        serializer = TestExecutionMetricsSerializer(data=request.data)
        if serializer.is_valid():
            session = Session()
            try:
                instance = serializer.create(serializer.validated_data)
                session.add(instance)
                session.commit()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            finally:
                session.close()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        session = Session()
        try:
            instance = session.query(TestExecutionMetrics).filter_by(matric_uuid=pk).first()
            if instance:
                serializer = TestExecutionMetricsSerializer(instance, data=request.data)
                if serializer.is_valid():
                    serializer.update(instance, serializer.validated_data)
                    session.commit()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_404_NOT_FOUND)
        finally:
            session.close()

    def delete(self, request, pk):
        session = Session()
        try:
            instance = session.query(TestExecutionMetrics).filter_by(matric_uuid=pk).first()
            if instance:
                session.delete(instance)
                session.commit()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(status=status.HTTP_404_NOT_FOUND)
        finally:
            session.close()


class MetadataAPIView(APIView):
    def get(self, request, pk=None):
        session = Session()
        try:
            if pk:
                instance = session.query(TestMetadataTable).filter_by(matric_uuid=pk).first()
                serializer = TestMetadataSerializer(instance)
            else:
                queryset = session.query(TestMetadataTable).all()
                serializer = TestMetadataSerializer(queryset, many=True)
            return Response(serializer.data)
        finally:
            session.close()

    def post(self, request):
        serializer = TestMetadataSerializer(data=request.data)
        if serializer.is_valid():
            session = Session()
            try:
                instance = serializer.create(serializer.validated_data)
                session.add(instance)
                session.commit()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            finally:
                session.close()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        session = Session()
        try:
            instance = session.query(TestMetadataTable).filter_by(matric_uuid=pk).first()
            if instance:
                serializer = TestMetadataSerializer(instance, data=request.data)
                if serializer.is_valid():
                    serializer.update(instance, serializer.validated_data)
                    session.commit()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_404_NOT_FOUND)
        finally:
            session.close()

    def delete(self, request, pk):
        session = Session()
        try:
            instance = session.query(TestMetadataTable).filter_by(matric_uuid=pk).first()
            if instance:
                session.delete(instance)
                session.commit()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(status=status.HTTP_404_NOT_FOUND)
        finally:
            session.close()

# class SQLAlchemySendRCVAPIView(APIView):
#     def get(self, request, pk=None):
#         session = Session()
#         try:
#             if pk:
#                 instance = session.query(SQLAlchemySendRCV).get(pk)
#                 serializer = SendRCVSerializer(instance)
#             else:
#                 queryset = session.query(SQLAlchemySendRCV).all()
#                 serializer = SendRCVSerializer(queryset, many=True)
#             return Response(serializer.data)
#         finally:
#             session.close()

#     def post(self, request):
#         serializer = SendRCVSerializer(data=request.data)
#         if serializer.is_valid():
#             session = Session()
#             instance = serializer.create(serializer.validated_data)
#             session.add(instance)
#             session.commit()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, pk):
#         session = Session()
#         try:
#             instance = session.query(SQLAlchemySendRCV).get(pk)
#             if instance:
#                 serializer = SendRCVSerializer(instance, data=request.data)
#                 if serializer.is_valid():
#                     serializer.update(instance, serializer.validated_data)
#                     session.commit()
#                     return Response(serializer.data)
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         finally:
#             session.close()

#     def delete(self, request, pk):
#         session = Session()
#         try:
#             instance = session.query(SQLAlchemySendRCV).get(pk)
#             if instance:
#                 session.delete(instance)
#                 session.commit()
#                 return Response(status=status.HTTP_204_NO_CONTENT)
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         finally:
#             session.close()


# class SQLAlchemyComparePairsAPIView(APIView):
#     def get(self, request, pk=None):
#         session = Session()
#         try:
#             if pk:
#                 instance = session.query(SQLAlchemyComparePairs).get(pk)
#                 serializer = ComparePair_Serializer(instance)
#             else:
#                 queryset = session.query(SQLAlchemyComparePairs).all()
#                 serializer = ComparePair_Serializer(queryset, many=True)
#             return Response(serializer.data)
#         finally:
#             session.close()

#     def post(self, request):
#         serializer = ComparePair_Serializer(data=request.data)
#         if serializer.is_valid():
#             session = Session()
#             instance = SQLAlchemyComparePairs(**serializer.validated_data)
#             session.add(instance)
#             session.commit()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def get_object(self, pk):
#         session = Session()
#         instance = session.query(SQLAlchemyComparePairs).get(pk)
#         return instance

#     def get(self, request, pk=None):
#         instance = self.get_object(pk)
#         if instance:
#             serializer = ComparePair_Serializer(instance)
#             return Response(serializer.data)
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     def put(self, request, pk=None):
#         instance = self.get_object(pk)
#         if instance:
#             serializer = ComparePair_Serializer(instance, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     def patch(self, request, pk=None):
#         instance = self.get_object(pk)
#         if instance:
#             serializer = ComparePair_Serializer(instance, data=request.data, partial=True)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     def delete(self, request, pk=None):
#         instance = self.get_object(pk)
#         if instance:
#             session = Session()
#             session.delete(instance)
#             session.commit()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         return Response(status=status.HTTP_404_NOT_FOUND)