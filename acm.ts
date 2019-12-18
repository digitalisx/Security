import Vorpal from 'vorpal';
import { setCredentials } from '../utils/aws/credentials';
import { ACM } from 'aws-sdk';

export function acm(vorpal: Vorpal) {
    new Command(vorpal)
}

class Command {
    constructor(private vorpal: Vorpal) {
        vorpal
            .command("acm ls")
            .option("--aws-profile <awsProfile>", "Add AWS Profile")
            .action((args) => this.show(args))
        vorpal
            .command("acm rm")
            .option("--aws-profile <awsProfile>", "Add AWS Profile")
            .option("--domain-name <DomainName>", "Add Remove Domain Name of Cert")
            .action((args) => this.remove(args))
    }

    async show(args: Vorpal.Args){
        const aws_profile = args.options["aws-profile"]
        setCredentials(aws_profile)
        await this.showCertificates()
    }

    async remove(args: Vorpal.Args){
        const aws_profile = args.options["aws-profile"]
        setCredentials(aws_profile)
        await this.removeCertificates(args.options["domain-name"])
    }

    async showCertificates(){
        const acm = new ACM()
        const cert_obj = await acm.listCertificates().promise()
        const cert_json = cert_obj.CertificateSummaryList!
        const certificateArns= cert_json.map((cert)=> cert.CertificateArn)
        const certificateDomains = cert_json.map((cert)=>cert.DomainName)

        const Table = require("cli-table3")
        const table = new Table({
            head: ['ARN', 'DOMAIN', 'EXPIRE DATE'],
            wordWrap: true
        })

        for(var index=0; index<certificateArns.length; index++){
            const cert_arn = certificateArns[index]!
            const cert_desc = await acm.describeCertificate({"CertificateArn":cert_arn}).promise()
            const cert_expire = cert_desc.Certificate!['NotAfter']
            table.push([cert_arn.split("/")[1], certificateDomains[index],
                        cert_expire])
        }
        console.log(table.toString())
    }

    async removeCertificates(arn: string){
        const acm = new ACM()
        const rm_response = await acm.deleteCertificate({"CertificateArn":arn}).promise()
        console.log(rm_response)
    }
}
