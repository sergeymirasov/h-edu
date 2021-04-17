from rest_framework import serializers

from prof_education.users.models import CommitteeMember

from .models import (
    Enrollee,
    EnrolleePassport,
    EnrolleeSpecialization,
    GraduatedInstitution,
    GosOlympiadStatus,
    WsrOlympiadStatus,
    AbylimpixStatus,
    SportAchievement,
    ParentData,
    EducationDoc,
)


class EnrolleePassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnrolleePassport
        fields = serializers.ALL_FIELDS


class EnrolleeSpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnrolleeSpecialization
        fields = serializers.ALL_FIELDS


class GraduatedInstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GraduatedInstitution
        fields = serializers.ALL_FIELDS


class GosOlympiadStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = GosOlympiadStatus
        fields = serializers.ALL_FIELDS


class WsrOlympiadStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = WsrOlympiadStatus
        fields = serializers.ALL_FIELDS


class AbylimpixStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbylimpixStatus
        fields = serializers.ALL_FIELDS


class SportAchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportAchievement
        fields = serializers.ALL_FIELDS


class ParentDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentData
        fields = serializers.ALL_FIELDS


class EducationDocSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationDoc
        fields = serializers.ALL_FIELDS


class CurrentUserOrgDefault:
    requires_context = True

    def __call__(self, serializer_field):
        committee_member = CommitteeMember.objects.get(
            pk=serializer_field.context["request"].user.pk
        )
        return committee_member.org

    def __repr__(self):
        return "%s()" % self.__class__.__name__


class EnrolleeSerializer(serializers.ModelSerializer):
    passport = EnrolleePassportSerializer()
    directions = EnrolleeSpecializationSerializer(many=True)
    graduated_institution = GraduatedInstitutionSerializer()
    gos_olympiad_status = GosOlympiadStatusSerializer()
    wsr_olympiad_status = WsrOlympiadStatusSerializer()
    abylimpix_status = AbylimpixStatusSerializer()
    sport_achievements = SportAchievementSerializer(many=True)
    mother = ParentDataSerializer()
    father = ParentDataSerializer()
    education_doc = EducationDocSerializer()
    education_org = serializers.HiddenField(default=CurrentUserOrgDefault())

    class Meta:
        model = Enrollee
        fields = serializers.ALL_FIELDS

    def create(self, validated_data):
        directions_data = validated_data.pop("directions", [])
        sport_achievements_data = validated_data.pop("sport_achievements", [])
        enrollee = Enrollee.objects.create(
            passport=self.save_relation(validated_data, "passport", EnrolleePassport),
            graduated_institution=self.save_relation(
                validated_data, "graduated_institution", GraduatedInstitution
            ),
            gos_olympiad_status=self.save_relation(
                validated_data, "gos_olympiad_status", GosOlympiadStatus
            ),
            wsr_olympiad_status=self.save_relation(
                validated_data, "wsr_olympiad_status", WsrOlympiadStatus
            ),
            abylimpix_status=self.save_relation(
                validated_data, "abylimpix_status", AbylimpixStatus
            ),
            mother=self.save_relation(validated_data, "mother", ParentData),
            father=self.save_relation(validated_data, "father", ParentData),
            education_doc=self.save_relation(
                validated_data, "education_doc", EducationDoc
            ),
            **validated_data,
        )
        self.save_directions(enrollee, directions_data)
        self.save_sport_achievements(enrollee, sport_achievements_data)
        return enrollee

    def save_relation(self, validated_data, rel_name, model):
        data = validated_data.pop(rel_name, None)
        return model.objects.create(**data) if data else None

    def save_directions(self, enrollee, directions_data):
        for direction_data in directions_data:
            enrollee.directions.create(**direction_data)

    def save_sport_achievements(self, enrollee, sport_achievements_data):
        for sport_achievement_data in sport_achievements_data:
            enrollee.sport_achievements.create(**sport_achievement_data)
