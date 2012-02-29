from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from zope.configuration import xmlconfig


class CfarThemeSandBoxLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import avrc.cfar.theme as package
        xmlconfig.file('configure.zcml', package, context=configurationContext)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'avrc.cfar.theme:default')


CFAR_THEME_FIXTURE = CfarThemeSandBoxLayer()

CFAR_THEME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(CFAR_THEME_FIXTURE,),
    name='CfarTheme:Integration'
    )

CFAR_THEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(CFAR_THEME_FIXTURE,),
    name='CfarTheme:Functional'
    )
