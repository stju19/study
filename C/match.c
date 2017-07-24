#include <stdio.h>
#include <string.h>

void StringKeyMatch(char *pAdapterDesc, char *pRegPciDesc)
{
    char *savePoint = NULL;
    char *RegDescFirstStr = NULL;
    char *cpAdapterPortIndex = NULL;
    char *cpRegPortIndex = NULL;
    char cTmpPciDesc[100];
    printf("AdapterDesc: %s\n", pAdapterDesc);
    printf("RegPciDesc:  %s\n", pRegPciDesc);

    char *result="match faild";
    if(0 == strcmp(pAdapterDesc,pRegPciDesc) )
    {
        result="match OK";
    }
    if (NULL != (cpAdapterPortIndex = strstr(pAdapterDesc,"#")))/*find #*/
    {
        if (NULL != (cpRegPortIndex = strstr(pRegPciDesc,"#")))/*find #*/
        {
            strcpy(cTmpPciDesc,pRegPciDesc);
            RegDescFirstStr = strtok(cTmpPciDesc,"#");
            printf("%s\n", RegDescFirstStr);
            printf("%s\n", cpRegPortIndex);
            printf("%s\n", pAdapterDesc);
            printf("%d\n", strstr(pAdapterDesc,RegDescFirstStr));
            printf("%d\n", strstr(pAdapterDesc,cpRegPortIndex));
            if ( (NULL != strstr(pAdapterDesc,RegDescFirstStr))&&(NULL != strstr(pAdapterDesc,cpRegPortIndex)) )
            {
                result="match OK";
            }
        }
    }
    else
    {
        printf("%d\n", strstr(pAdapterDesc,"(NDIS VBD"));
        printf("%d\n", strstr(pAdapterDesc,pRegPciDesc));
        if ( (')' == pAdapterDesc[strlen(pAdapterDesc)-1])&&(NULL != strstr(pAdapterDesc,pRegPciDesc)) )
        {
            result="match OK";
        }
    }
    printf("%s\n\n", result);
}

int main()
{
    StringKeyMatch("abc", "abc");
    StringKeyMatch("Broadcom BCM57810 NetXtreme II 10 GigE(NDIS VBD客户端)", "Broadcom BCM57810 NetXtreme II 10 GigE");
    StringKeyMatch("Broadcom BCM57810 NetXtreme II 10 GigE(NDIS VBD客户端) #23", "Broadcom BCM57810 NetXtreme II 10 GigE #23");
    StringKeyMatch("Intel(R) Ethernet Converged Network Adapter X710", "Intel(R) Ethernet Converged Network Adapter X710");
    StringKeyMatch("Intel(R) Ethernet Converged Network Adapter X710-2", "Intel(R) Ethernet Converged Network Adapter X710-2");
    StringKeyMatch("Intel(R) Ethernet Converged Network Adapter X710-2", "Intel(R) Ethernet Converged Network Adapter X710");
    StringKeyMatch("Intel(R) Ethernet Converged Network Adapter X710", "Intel(R) Ethernet Converged Network Adapter X710-2");
}
