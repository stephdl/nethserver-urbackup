<?php
namespace NethServer\Module\Dashboard\Applications;
/**
 * Urbackup web interface
 *
 * @author stephane de labrusse
 */
class Urbackup extends \Nethgui\Module\AbstractModule implements \NethServer\Module\Dashboard\Interfaces\ApplicationInterface
{
    public function getName()
    {
        return "Urbackup";
    }
    public function getInfo()
    {
         $webapp = $this->getPlatform()->getDatabase('configuration')->getProp('urbackup-server','Name');
         $host = explode(':',$_SERVER['HTTP_HOST']);
         return array(
            'url_Urbackup' => "https://".$host[0]."/$webapp/"
         );
    }
}
