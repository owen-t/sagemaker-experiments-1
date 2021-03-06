# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
"""Contains the TrialComponent class."""
from smexperiments import _base_types, api_types


class TrialComponent(_base_types.Record):
    """
    This class represents a SageMaker trial component object.

    A trial component is a stage in a trial.

    Trial components are created automatically within the SageMaker runtime and may not be created directly.
    To automatically associate trial components with a trial and experiment supply an experiment config when creating a
    job. For example: https://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateTrainingJob.html
    """

    trial_component_name = None
    trial_component_arn = None
    display_name = None
    source = None
    status = None
    start_time = None
    end_time = None
    creation_time = None
    created_by = None
    last_modified_time = None
    last_modified_by = None
    parameters = None
    input_artifacts = None
    output_artifacts = None
    metrics = None

    _boto_load_method = "describe_trial_component"
    _boto_create_method = "create_trial_component"
    _boto_update_method = "update_trial_component"
    _boto_delete_method = "delete_trial_component"

    _custom_boto_types = {
        "source": (api_types.TrialComponentSource, False),
        "status": (api_types.TrialComponentStatus, False),
        "parameters": (api_types.TrialComponentParameters, False),
        "input_artifacts": (api_types.TrialComponentArtifact, True),
        "output_artifacts": (api_types.TrialComponentArtifact, True),
        "metrics": (api_types.TrialComponentMetricSummary, True),
    }

    _boto_update_members = [
        "trial_component_name",
        "display_name",
        "status",
        "start_time",
        "end_time",
        "parameters",
        "input_artifacts",
        "output_artifacts",
    ]
    _boto_delete_members = ["trial_component_name"]

    @classmethod
    def _boto_ignore(cls):
        return super(TrialComponent, cls)._boto_ignore() + ["CreatedBy"]

    def save(self):
        """Save the state of this TrialComponent to SageMaker."""
        return self._invoke_api(self._boto_update_method, self._boto_update_members)

    def delete(self):
        """Delete this TrialComponent from SageMaker."""
        self._invoke_api(self._boto_delete_method, self._boto_delete_members)

    @classmethod
    def load(cls, trial_component_name, sagemaker_boto_client=None):
        """
        Load an existing trial component and return an ``TrialComponent`` object representing it.

        Args:
            trial_component_name (str): Name of the trial component
            sagemaker_boto_client (SageMaker.Client, optional): Boto3 client for SageMaker.
                If not supplied, a default boto3 client will be created and used.
        Returns:
            smexperiments.trial_component.TrialComponent: A SageMaker ``TrialComponent`` object
        """
        trial_component = cls._construct(
            cls._boto_load_method,
            trial_component_name=trial_component_name,
            sagemaker_boto_client=sagemaker_boto_client,
        )
        return trial_component

    @classmethod
    def create(cls, trial_component_name, display_name=None, sagemaker_boto_client=None):
        """
        Create a trial component and return a ``TrialComponent`` object representing it.

        Returns:
            smexperiments.trial_component.TrialComponent: A SageMaker ``TrialComponent``
                object.
        """
        return super(TrialComponent, cls)._construct(
            cls._boto_create_method,
            trial_component_name=trial_component_name,
            display_name=display_name,
            sagemaker_boto_client=sagemaker_boto_client,
        )

    @classmethod
    def list(
        cls,
        source_arn=None,
        created_before=None,
        created_after=None,
        sort_by=None,
        sort_order=None,
        sagemaker_boto_client=None,
        trial_name=None,
        experiment_name=None,
        max_results=None,
        next_token=None,
    ):
        """
        Return a list of trial component summaries.

        Args:
            source_arn (str, optional): A SageMaker Training or Processing Job ARN.
            created_before (datetime.datetime, optional): Return trial components created before this instant.
            created_after (datetime.datetime, optional): Return trial components created after this instant.
            sort_by (str, optional): Which property to sort results by. One of 'SourceArn', 'CreatedBefore',
                'CreatedAfter'
            sort_order (str, optional): One of 'Ascending', or 'Descending'.
            sagemaker_boto_client (SageMaker.Client, optional) : Boto3 client for SageMaker.
                If not supplied, a default boto3 client will be created and used.
            trial_name (str, optional): Name of a Trial
            experiment_name (str, optional): Name of an Experiment
            max_results (int, optional): maximum number of trial components to retrieve
            next_token (str, optional): token for next page of results

        Returns:
            collections.Iterator[smexperiments.api_types.TrialComponentSummary]: An iterator
                over ``TrialComponentSummary`` objects.
        """
        return super(TrialComponent, cls)._list(
            "list_trial_components",
            api_types.TrialComponentSummary.from_boto,
            "TrialComponentSummaries",
            source_arn=source_arn,
            created_before=created_before,
            created_after=created_after,
            sort_by=sort_by,
            sort_order=sort_order,
            sagemaker_boto_client=sagemaker_boto_client,
            trial_name=trial_name,
            experiment_name=experiment_name,
            max_results=max_results,
            next_token=next_token,
        )
