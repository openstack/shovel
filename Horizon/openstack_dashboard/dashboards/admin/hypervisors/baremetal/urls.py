# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from django.conf.urls import patterns
from django.conf.urls import url

from openstack_dashboard.dashboards.admin.hypervisors.baremetal import views

urlpatterns = patterns(
    'openstack_dashboard.dashboards.admin.hypervisors.baremetal.views',
    url(r'^(?P<baremetal>[^/]+)/register$', views.RegisterView.as_view(), name='register'),
    url(r'^(?P<baremetal>[^/]+)/unregister$', views.UnregisterView.as_view(), name='unregister'),
    url(r'^(?P<baremetal>[^/]+)/detail$', views.BareMetalDetailView.as_view(), name='detail'),
    url(r'^(?P<baremetal>[^/]+)/events$', views.BareMetalEventView.as_view(), name='events'),
    url(r'^(?P<baremetal>[^/]+)/failover$', views.FailoverView.as_view(), name='failover'),
)
