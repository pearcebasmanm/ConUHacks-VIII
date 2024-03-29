import type { NextApiRequest, NextApiResponse } from 'next';
import { MongoClient, ServerApiVersion } from 'mongodb';

const handler = async (req: NextApiRequest, res: NextApiResponse) => {
    const uri = "mongodb+srv://ADMIN:qwe123qwe123@cluster0.uspsoud.mongodb.net/?retryWrites=true&w=majority";
    const dbName = 'Schedule_Optimization';

    if (!uri || !dbName) {
        res.status(500).json({ message: 'Environment variables MONGODB_URI and MONGODB_DB must be set' });
        return;
    }

    const client = new MongoClient(uri, {
        serverApi: {
            version: ServerApiVersion.v1,            
            strict: true,
            deprecationErrors: false
        }
    })
    
    try {
        await client.connect();
        
        const db = client.db(dbName);
        let data : any[] = [], date;

        if (req.query.date) {
            date = req.query.date;
        }

        res.status(200).json(data);
    } catch (error : any) {
        res.status(500).json({ message: error.message });
    } finally {
        client.close();
    }
};

export default handler;
